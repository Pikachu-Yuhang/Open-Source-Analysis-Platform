from django.db import models

# Create your models here.

class Repo(models.Model):
    id = models.CharField(max_length=63, primary_key=True)
    full_name = models.CharField(max_length=63)


class ResultCache(models.Model):
    class Type(models.TextChoices):
        IssueInfo = 'I'
        OtherInfo = 'O'
        PRInfo = 'PR'
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
    )
    result = models.TextField()
    updated_time = models.DateTimeField()


class RepoBasicInfoCache(models.Model):
    class InfoType(models.TextChoices):
        Issue = 'I'
        PullRequest = 'P'
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=1,
        choices=InfoType.choices,
    )
    ids = models.TextField()
    updated_time = models.DateTimeField()
    next_page = models.IntegerField(default=0) # for issue and pr pulling


class Actor(models.Model):
    id = models.CharField(max_length=31, primary_key=True)
    company = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)


class Issue(models.Model):
    id = models.CharField(max_length=63, primary_key=True)
    number = models.IntegerField()
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    commenter_ids = models.TextField() # with duplicates
    first_response_time = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PullRequest(models.Model):
    id = models.CharField(max_length=63, primary_key=True)
    number = models.IntegerField()
    creator = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    reviewer_ids = models.TextField() # with duplicates
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()