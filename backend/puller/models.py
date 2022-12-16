from django.db import models

# Create your models here.

class Batch(models.Model):
    repo_paths = models.TextField() # array of size m
    time_intervals = models.TextField() # array of size n * 2


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
        Fork = 'F',
        Issue = 'I',
        Member = 'M'
        Push = 'P',
        PullRequest = 'PR',
        Watch = 'W'
    class Action(models.TextChoices):
        Added = 'A',
        Commented = 'Co',
        Closed = 'Cl',
        Opened = 'O',
        Removed = 'Rm',
        Reviewed = 'Rv'

    id = models.CharField(max_length=31, primary_key=True)
    full_type = models.CharField(max_length=31)
    type = models.CharField(
        max_length=2,
        choices=EventType.choices,
    )
    action = models.CharField(
        max_length=2,
        choices=Action.choices,
    )
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
    )
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField()
    additional_info = models.TextField()