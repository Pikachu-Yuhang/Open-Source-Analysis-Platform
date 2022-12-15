import datetime, json, queue
import numpy
from github import Github

from .models import Actor, CompanyNameMatch, Issue, PullRequest, ResultCache, Repo, RepoBasicInfoCache

class Fetcher:
    def __init__(self, token, fetch_limit=100):
        self.g = Github(token)
        self.fetch_limit = fetch_limit
        self.q = queue.Queue()

    def get_repo_obj(self, repo):
        obj = None
        try:
            obj = Repo.objects.get(pk=repo.id)
        except:
            obj = Repo(id=repo.id, full_name=repo.full_name)
            obj.save()
        return obj
    
    def get_actor_obj(self, usr):
        obj = None
        try:
            obj = Actor.objects.get(pk=usr.id)
        except:
            obj = Actor(id=usr.id, email=usr.email, company=usr.company)
            obj.save()
        return obj

    def get_issue_obj(self, issue):
        obj = None
        try:
            obj = Issue.objects.get(pk=issue.id)
        except:
            obj = Issue(
                id=issue.id,
                number=issue.number,
                repo=self.get_repo_obj(issue.repository),
                creator=self.get_actor_obj(issue.user),
                commenter_ids=json.dumps([]),
                first_response_time=datetime.datetime(2100, 1, 1),
                created_at=issue.created_at,
                updated_at=issue.updated_at,
            )
            obj.save()
        return obj

    def get_pr_obj(self, pr):
        obj = None
        try:
            obj = PullRequest.objects.get(pk=pr.id)
        except:
            obj = PullRequest(
                id=pr.id,
                number=pr.number,
                creator=self.get_actor_obj(pr.user),
                reviewer_ids=json.dumps([]),
                created_at=pr.created_at,
                updated_at=pr.updated_at,
            )
            obj.save()
        return obj

    def get_result_cache_obj(self, repo_path:str, type:ResultCache.Type):
        repo = self.g.get_repo(repo_path)
        repo_obj = self.get_repo_obj(repo)
        records, record = ResultCache.objects.filter(repo=repo_obj, type=type), None
        if len(records) > 0:
            record = records[0]
        else:
            record = ResultCache(repo=repo_obj, type=type, result=json.dumps({}), updated_time=datetime.datetime.now())
            record.save()
        return record

    def get_repo_basic_info_cache_obj(self, repo_path:str, type:RepoBasicInfoCache.InfoType):
        repo = self.g.get_repo(repo_path)
        repo_obj = self.get_repo_obj(repo)
        records, record = RepoBasicInfoCache.objects.filter(repo=repo_obj, type=type), None
        if len(records) > 0:
            record = records[0]
        else:
            record = RepoBasicInfoCache(repo=repo_obj, type=type, ids=json.dumps([]), updated_time=datetime.datetime.now())
            record.save()
        return record

    def get_issues_at(self, repo_path:str, page_id:int):
        repo = self.g.get_repo(repo_path)
        all, res, next_page = repo.get_issues(state='all', sort='created', direction='asc'), [], page_id
        page_issues = all.get_page(page_id)
        if len(page_issues) > 0:
            try:
                for issue in page_issues:
                    if issue.pull_request is None:
                        self.get_issue_obj(issue)
                        res.append(issue.id)
                next_page += 1
            except:
                res.clear()
        else:
            next_page = -1
        res.reverse()
        return res, next_page

    def get_prs_at(self, repo_path:str, page_id:int):
        repo = self.g.get_repo(repo_path)
        all, res, next_page = repo.get_pulls(state='all', sort='created', direction='asc'), [], page_id
        page_prs = all.get_page(page_id)
        if len(page_prs) > 0:
            try:
                for pr in page_prs:
                    self.get_pr_obj(pr)
                    res.append(pr.id)
                next_page += 1
            except:
                res.clear()
        else:
            next_page = -1
        res.reverse()
        return res, next_page

    def get_issues_from(self, repo_path:str, from_id:str):
        repo = self.g.get_repo(repo_path)
        all, res = repo.get_issues(state='all', sort='created', direction='desc'), []
        for issue in all:
            if issue.id == from_id:
                break
            if issue.pull_request is None:
                self.get_issue_obj(issue)
                res.append(issue.id)
        return res

    def get_prs_from(self, repo_path:str, from_id:str):
        repo = self.g.get_repo(repo_path)
        all, res = repo.get_pulls(state='all', sort='created', direction='desc'), []
        for pull in all:
            if pull.id == from_id:
                break
            self.get_pr_obj(pull)
            res.append(pull.id)
        return res

    def get_result_cache(self, repo_path:str, type:ResultCache.Type):
        obj = self.get_result_cache_obj(repo_path, type)
        return json.loads(obj.result), obj.updated_time

    def group_by_company(self, actor_ids_dup):
        company_name_map = {pair.name: pair.map_to for pair in CompanyNameMatch.objects.all()}
        id_to_actor_obj, res = {id: Actor.objects.get(pk=id) for id in set(actor_ids_dup)}, dict()
        for actor_id in actor_ids_dup:
            actor_obj, k = id_to_actor_obj[actor_id], None
            try:
                k = company_name_map[k]
            except:
                k = actor_obj.company
            res[k] = res.setdefault(k, 0) + 1
        return res

    def get_result_cache_issue_info(self, basic_info:RepoBasicInfoCache):
        issue_ids = json.loads(basic_info.ids)
        issue_objs = Issue.objects.filter(pk__in=issue_ids)

        repo = self.g.get_repo(basic_info.repo.full_name)
        for issue_obj in issue_objs:
            issue = repo.get_issue(issue_obj.number)
            if issue.updated_at.timestamp() > issue_obj.updated_at.timestamp():
                comments, commenter_ids = issue.get_comments(), []
                # TODO: use self-implemented fetcher
                for comment in comments:
                    commenter_ids.append(comment.user.id)
                    if comment.created_at < issue_obj.first_response_time:
                        issue_obj.first_response_time = comment.created_at # robust
                issue_obj.commenter_ids = json.dumps(commenter_ids)
                issue_obj.updated_at = issue_obj.updated_at
                issue_obj.save()
        
        creator_ids_dup, comment_cnt, commenter_ids_dup, month_to_frt = [], 0, [], dict()
        for issue_obj in issue_objs:
            creator_ids_dup.append(issue_obj.creator.id)
            commenter_id_list = json.loads(issue_obj.commenter_ids)
            comment_cnt += len(commenter_id_list)
            commenter_ids_dup += commenter_id_list
            if issue_obj.first_response_time > issue_obj.created_at:
                k = issue_obj.created_at.strftime("%Y-%m")
                list = month_to_frt.setdefault(k, [])
                month_to_frt[k].append(issue_obj.first_response_time - issue_obj.created_at)
        return {
            'issue_cnt': len(issue_ids),
            'issue_creator_cnt': len(set(creator_ids_dup)),
            'comment_cnt': comment_cnt,
            'commenter_cnt': len(set(commenter_ids_dup)),
            'issue_by_company': self.group_by_company(creator_ids_dup),
            'first_response_by_month': {k: [numpy.percentile(month_to_frt[k], 25*i) for i in range(0, 5)] for k in month_to_frt}
        }

    def get_result_cache_pr_info(self, basic_info:RepoBasicInfoCache):
        pr_ids = json.loads(basic_info.ids)
        pr_objs = PullRequest.objects.filter(pk__in=pr_ids)

        repo = self.g.get_repo(basic_info.repo.full_name)
        for pr_obj in pr_objs:
            pr = repo.get_pull(pr_obj.number)
            if pr.updated_at.timestamp() > pr_obj.updated_at.timestamp():
                reviews, reviewer_ids = pr.get_reviews(), []
                # TODO: use self-implemented fetcher
                for review in reviews:
                    reviewer_ids.append(review.user.id)
                pr_obj.reviewer_ids = json.dumps(reviewer_ids)
                pr_obj.updated_at = pr.updated_at
                pr_obj.save()

        creator_ids_dup, review_cnt, reviewer_ids_dup = [], 0, []
        for pr_obj in pr_objs:
            creator_ids_dup.append(pr_obj.creator.id)
            reviewer_ids_list = json.loads(pr_obj.reviewer_ids)
            review_cnt += len(reviewer_ids_list)
            reviewer_ids_dup += reviewer_ids_list
        return {
            'pr_cnt': len(pr_ids),
            'pr_creator_cnt': len(set(creator_ids_dup)),
            'pr_review_cnt': review_cnt,
            'pr_reviewer_cnt': len(set(reviewer_ids_dup)),
            'pr_by_company': self.group_by_company(creator_ids_dup)
        }

    def update_result_cache(self, repo_path, result_type):
        # Call update_repo_basic_info_cache first.
        issue_info, pull_info = (
            self.get_repo_basic_info_cache_obj(repo_path, RepoBasicInfoCache.InfoType.Issue),
            self.get_repo_basic_info_cache_obj(repo_path, RepoBasicInfoCache.InfoType.PullRequest)
        )
        record = self.get_result_cache_obj(repo_path, result_type)
        match result_type:
            case ResultCache.Type.IssueInfo:
                record.result = json.dumps(self.get_result_cache_issue_info(issue_info), default=str)
                record.updated_time = issue_info.updated_time
            case ResultCache.Type.OtherInfo:
                repo = self.g.get_repo(repo_path)
                record.result = json.dumps({
                    'star_cnt': repo.stargazers_count,
                    'commit_cnt': repo.get_commits().totalCount,
                    'fork_cnt' : repo.forks_count,
                })
                record.updated_time = datetime.datetime.now()
            case ResultCache.Type.PRInfo:
                record.result = json.dumps(self.get_result_cache_pr_info(pull_info), default=str)
                record.updated_time = pull_info.updated_time
        record.save()

    def update_repo_basic_info_cache(self, repo_path, info_type):
        record = self.get_repo_basic_info_cache_obj(repo_path, info_type)

        match info_type:
            case RepoBasicInfoCache.InfoType.Issue:
                issue_ids, page, new_issue_ids = json.loads(record.ids), record.next_page, None
                if page >= 0:
                    new_issue_ids, record.next_page = self.get_issues_at(repo_path, page)
                else:
                    from_id = issue_ids[0]
                    new_issue_ids = self.get_issues_from(repo_path, from_id)
                record.ids = json.dumps(new_issue_ids + issue_ids)
            case RepoBasicInfoCache.InfoType.PullRequest:
                pr_ids, page, new_pr_ids = json.loads(record.ids), record.next_page, None
                if page >= 0:
                    new_pr_ids, record.next_page = self.get_prs_at(repo_path, page)
                else:
                    from_id = pr_ids[0]
                    new_pr_ids = self.get_prs_from(repo_path, from_id)
                record.ids = json.dumps(new_pr_ids + pr_ids)
        
        record.updated_time = datetime.datetime.now()
        record.save()

    def update(self):
        while True:
            repo_path = self.q.get()
            if not repo_path:
                self.q.task_done()
                break
            
            self.update_repo(repo_path)
            self.q.task_done()

    def update_repo(self, repo_path):
        fetcher.update_repo_basic_info_cache(repo_path, RepoBasicInfoCache.InfoType.Issue)
        fetcher.update_repo_basic_info_cache(repo_path, RepoBasicInfoCache.InfoType.PullRequest)

        fetcher.update_result_cache(repo_path, ResultCache.Type.IssueInfo)
        fetcher.update_result_cache(repo_path, ResultCache.Type.PRInfo)
        fetcher.update_result_cache(repo_path, ResultCache.Type.OtherInfo)


TOKEN = ""
fetcher = Fetcher(TOKEN)