import datetime, json
from github import Github

from .models import SnapshotCache

class Fetcher:
    def __init__(self, token):
        self.g = Github(token)

    def group_by_company(users):
        # TODO
        return {}

    def update_record(self, repo_path, type):
        records, record = SnapshotCache.objects.filter(repo_name=repo_path, type=type), None
        if len(records) == 0:
            record = SnapshotCache(repo_name=repo_path, type=type)
            record.save()
        else:
            record = records[0]

        repo = self.g.get_repo(repo_path)
        match type:
            case SnapshotCache.Type.Issue:
                issues = repo.get_issues()
                creators_dup = [issue.user for issue in issues]
                comments = repo.get_issues_comments()
                comment_creators_dup = [comment.user for comment in comments]
                record.result = json.dumps({
                    'open_issue_cnt': repo.open_issues_count,
                    'issue_creator_cnt': len(set([creator.id for creator in creators_dup])),
                    'issue_comment_cnt': comments.totalCount,
                    'issue_comment_creator_cnt': len(set([creator.id for creator in comment_creators_dup])),
                    'issue_by_company': Fetcher.group_by_company(creators_dup)
                })
            case SnapshotCache.Type.PullRequest:
                prs = repo.get_pulls()
                pr_creators_dup = [pr.user for pr in prs]

                reviews = []
                for pr in prs:
                    for review in pr.get_reviews():
                        reviews.append(review)
                reviewers_dup = [review.user for review in reviews]
                record.result = json.dumps({
                    'pr_cnt': prs.totalCount,
                    'pr_creator_cnt': len(set([creator.id for creator in pr_creators_dup])),
                    'pr_review_cnt': len(reviews),
                    'pr_reviewer_cnt': len(set([reviewer.id for reviewer in reviewers_dup])),
                    'pr_by_company': Fetcher.group_by_company(pr_creators_dup)
                })
            case SnapshotCache.Type.Other:
                record.result = json.dumps({
                    'star_cnt': repo.stargazers_count,
                    'commit_cnt': repo.get_commits().totalCount,
                    'fork_cnt' : repo.forks_count
                })
            case other:
                pass

        record.updated_at = datetime.datetime.now()
        record.save()
        pass


TOKEN = "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"
fetcher = Fetcher(TOKEN)