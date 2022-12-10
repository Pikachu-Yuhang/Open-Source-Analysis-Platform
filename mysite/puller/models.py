from django.db import models

# Create your models here.

class Watched(models.Model):
    repo_path = models.CharField('path')
    updated_till = models.DateField('date')


class Actor(models.Model):
    id = models.CharField(primary_key=True)
    company = models.CharField()
    url = models.CharField()


class Repo(models.Model):
    id = models.CharField(primary_key=True)
    full_name = models.CharField()
    url = models.CharField()


class Event(models.Model):
    class EventType(models.TextChoices):
        CommitCommentEvent = 'CC'
        ForkEvent = 'F'
        IssueCommentEvent = 'IC'
        IssuesEvent = 'I'
        MemberEvent = 'M'
        PullRequestEvent = 'PR'
        PullRequestReviewEvent = 'PRR'
        PullRequestReviewCommentEvent = 'PRRC'
        PullRequestReviewThreadEvent = 'PRRT'
        PushEvent = 'P'
        WatchEvent = 'W'

    event_type = models.CharField(
        max_length=4,
        choices=EventType.choices,
    )
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
