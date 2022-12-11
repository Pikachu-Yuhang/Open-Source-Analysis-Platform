from django.db import models

# Create your models here.

class Watched(models.Model):
    repo_path = models.CharField(max_length=63, primary_key=True)
    updated_till = models.DateField()


class Actor(models.Model):
    id = models.CharField(max_length=31, primary_key=True)
    company = models.CharField(max_length=63)
    url = models.CharField(max_length=255)


class Repo(models.Model):
    id = models.CharField(max_length=31, primary_key=True)
    full_name = models.CharField(max_length=63)
    url = models.CharField(max_length=255)


class Event(models.Model):
    class EventType(models.TextChoices):
        CommitCommentEvent = 'CC'
        CreateEvent = 'C'
        DeleteEvent = 'D'
        ForkEvent = 'F'
        GollumEvent = 'G'
        IssueCommentEvent = 'IC'
        IssuesEvent = 'I'
        MemberEvent = 'M'
        PublicEvent = 'Pub'
        PullRequestEvent = 'PR'
        PullRequestReviewEvent = 'PRR'
        PullRequestReviewCommentEvent = 'PRRC'
        PullRequestReviewThreadEvent = 'PRRT'
        PushEvent = 'P'
        ReleaseEvent = 'R'
        SponsorshipEvent = 'S'
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
    created_at = models.DateTimeField()
