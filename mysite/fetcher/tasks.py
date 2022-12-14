from github import Github

class Fetcher:
    def __init__(self, token):
        self.g = Github(token)

    def overview(self, repo_path):
        repo = self.g.get_repo(repo_path)
        
        return {
            'star_cnt': repo.stargazers_count,
            'commit_cnt': repo.get_commits().totalCount,
            'open_issue_cnt': repo.open_issues_count,
            'fork_cnt': repo.forks_count,
            'pr_creator_cnt': len(set([pull.user.id for pull in repo.get_pulls()]))
        }

    def what(self):
        pass


TOKEN = "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"
fetcher = Fetcher(TOKEN)