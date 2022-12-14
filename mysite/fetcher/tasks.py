import datetime
from github import Github

class Fetcher:
    def __init__(self, token):
        self.g = Github(token)

    def update_overview(self, obj):
        repo = self.g.get_repo(obj.repo_name)

        obj.star_cnt = repo.stargazers_count
        obj.commit_cnt = repo.get_commits().totalCount
        obj.open_issue_cnt = repo.open_issues_count
        obj.fork_cnt = repo.forks_count
        obj.pr_creator_cnt = len(set([pull.user.id for pull in repo.get_pulls()]))
        obj.updated_at = datetime.datetime.now()


TOKEN = ""
fetcher = Fetcher(TOKEN)