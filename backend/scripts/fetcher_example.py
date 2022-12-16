from fetcher.tasks import fetcher
repo_path = 'pytorch/pytorch'
while True:
    fetcher.update_repo(repo_path)