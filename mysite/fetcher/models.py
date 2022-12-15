from django.db import models

# Create your models here.

class Repo(models.Model):
    id = models.CharField(max_length=63, primary_key=True)
    full_name = models.CharField(max_length=63)


class ResultCache(models.Model):
    class Type(models.TextChoices):
        CompanyInfo = 'Ci'
        IssueOverview = 'Io'
        IssueFirstResponseTime = 'Ifrt'
        OtherInfo = 'Oi'
        PROverview = 'PRo'
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=4,
        choices=Type.choices,
    )
    result = models.TextField()
    updated_time = models.DateTimeField()


class RepoBasicInfoCache(models.Model):
    class InfoType(models.TextChoices):
        Issue = 'I'
        PullRequest = 'P'
        Star = 'S'
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


class Actor(models.Model):
    id = models.CharField(max_length=31, primary_key=True)
    company = models.CharField(max_length=63)
    email = models.CharField(max_length=63)


class Issue(models.Model):
    id = models.CharField(max_length=63, primary_key=True)
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    creator = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    commenter_ids = models.TextField()
    first_response_time = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class PullRequest(models.Model):
    id = models.CharField(max_length=63, primary_key=True)
    creator = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    reviewer_ids = models.TextField()
    updated_at = models.DateTimeField()