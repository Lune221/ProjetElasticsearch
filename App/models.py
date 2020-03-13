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
    # running_time_secs = models.IntegerField()
    # actors = ArrayField(models.CharField(max_length=50))
    # directors = ArrayField(models.CharField(max_length=50))
    # release_date = models.DateTimeField()
    # rating = models.DecimalField(max_digits=4, decimal_places=2)
    # genres = ArrayField(models.CharField(max_length=50))
    # idi = models.CharField(max_length=10, primary_key=False)
    # type = models.CharField(max_length=10)

    def __str__(self):
        return self.title