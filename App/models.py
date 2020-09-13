from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Film(models.Model):
    image_url = models.URLField()
    plot = models.TextField(max_length=500)
    title = models.CharField(max_length=250)
    rank = models.IntegerField()
    year = models.IntegerField()
    type = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title

class Publication(models.Model):
    type = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=250, null=True)
    year = models.IntegerField(null=True)
    booktitle = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=250, null=True)
    authors = models.CharField(max_length=600, null=True)

    def __str__(self):
        return self.title
    