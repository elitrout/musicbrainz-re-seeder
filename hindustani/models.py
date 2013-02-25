from django.db import models

class Release(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    mbid = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    who = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title

class Track(models.Model):
    release = models.ForeignKey(Release)
    name = models.CharField(max_length=200)
    position = models.IntegerField()
    length = models.CharField(max_length=10)
    filename = models.CharField(max_length=255)
    disc = models.IntegerField()

    def __unicode__(self):
        return self.name

