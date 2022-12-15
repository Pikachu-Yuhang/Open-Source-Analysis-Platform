import datetime, json
from github import Github

from .models import ResultCache, Repo, RepoBasicInfoCache

class Fetcher:
    def __init__(self, token):
        self.g = Github(token)

    def get_repo_obj(self, repo_path):
        repo, obj = self.g.get_repo(repo_path), None
        try:
            obj = Repo.objects.get(pk=repo.id)
        except:
            obj = Repo(id=repo.id, full_name=repo.full_name)
            obj.save()
        return obj

    def get_result_cache_obj(self, repo_path, type):
        repo_obj, repo = self.get_repo_obj(repo_path), self.g.get_repo(repo_path)
        records, record = ResultCache.objects.filter(repo=repo_obj, type=type), None
        if len(records) > 0:
            record = records[0]
        else:
            record = ResultCache(repo=repo_obj, type=type, updated_time=datetime.datetime.now())
            record.save()
        return record

    def get_repo_basic_info_cache_obj(self, repo_path, type):
        repo_obj, repo = self.get_repo_obj(repo_path), self.g.get_repo(repo_path)
        records, record = RepoBasicInfoCache.objects.filter(repo=repo_obj, type=type), None
        if len(records) > 0:
            record = records[0]
        else:
            record = RepoBasicInfoCache(repo=repo_obj, type=type, ids=json.dumps([]), updated_time=datetime.datetime.now())
            record.save()
        return record

    def get_issues_from(self, repo_path, from_id):
        repo = self.g.get_repo(repo_path)
        all, res = repo.get_issues(state='all', sort='created', direction='desc'), []
        for issue in all:
            if issue.id == from_id:
                break
            if issue.pull_request is None:
                res.append(issue.id)
        return res

    def get_prs_from(self, repo_path, from_id):
        repo = self.g.get_repo(repo_path)
        all, res = repo.get_pulls(state='all', sort='created', direction='desc'), []
        for pull in all:
            if pull.id == from_id:
                break
            res.append(pull.id)
        return res

    def get_result_cache(self, repo_path, type):
        obj = self.get_result_cache_obj(repo_path, type)
        return json.loads(obj.result), obj.updated_time

    def update_result_cache(self, repo_path, result_type):
        record = self.get_result_cache_obj(repo_path, result_type)

        match result_type:
            case ResultCache.Type.CompanyInfo:
                # TODO
                pass
            case ResultCache.Type.IssueOverview:
                # TODO
                pass
            case ResultCache.Type.IssueFirstResponseTime:
                # TODO
                pass
            case ResultCache.Type.OtherInfo:
                # TODO
                pass
            case ResultCache.Type.PROverview:
                # TODO
                pass
        
        record.updated_time = datetime.datetime.now()
        record.save()

    def update_repo_basic_info_cache(self, repo_path, info_type):
        record = self.get_repo_basic_info_cache_obj(repo_path, info_type)

        match info_type:
            case RepoBasicInfoCache.InfoType.Issue:
                issue_ids, from_id = json.loads(record.ids), ''
                if len(issue_ids) > 0:
                    from_id = issue_ids[0]
                new_issue_ids = self.get_issues_from(repo_path, from_id)
                record.ids = json.dumps(new_issue_ids + issue_ids)
            case RepoBasicInfoCache.InfoType.PullRequest:
                pr_ids, from_id = json.loads(record.ids), ''
                if len(pr_ids) > 0:
                    from_id = pr_ids[0]
                new_pr_ids = self.get_prs_from(repo_path, from_id)
                record.ids = json.dumps(new_pr_ids + pr_ids)
            case RepoBasicInfoCache.InfoType.Star:
                repo = self.g.get_repo(repo_path)
                record.ids = json.dumps([usr.id for usr in repo.get_stargazers()])
        
        record.updated_time = datetime.datetime.now()
        record.save()


TOKEN = ""
fetcher = Fetcher(TOKEN)