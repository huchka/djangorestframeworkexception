from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    rank = models.IntegerField(blank=False, null=False, default=10)
    content = models.CharField(max_length=100, blank=False, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
