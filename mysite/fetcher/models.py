from django.db import models

# Create your models here.

class SnapshotCache(models.Model):
    class Type(models.TextChoices):
        Issue = 'I',
        PullRequest = 'P',
        Other = 'O'
    repo_name = models.CharField(max_length=63)
    type = models.CharField(
        max_length=1,
        choices=Type.choices,
    )
    result = models.TextField()
    updated_at = models.DateTimeField()