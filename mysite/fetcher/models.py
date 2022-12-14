from django.db import models

# Create your models here.

class Overview(models.Model):
    repo_name = models.CharField(max_length=63, primary_key=True)
    star_cnt = models.IntegerField()
    commit_cnt = models.IntegerField()
    open_issue_cnt = models.IntegerField()
    fork_cnt = models.IntegerField()
    pr_creator_cnt = models.IntegerField()
    updated_at = models.DateTimeField()