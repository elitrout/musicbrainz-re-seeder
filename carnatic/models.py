from django.db import models

# Create your models here.

class Release(models.Model):
    title = models.CharField(max_length=200)
    albumid = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    mbid = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Track(models.Model):
    release = models.ForeignKey(Release)
    name = models.CharField(max_length=200)
    raga = models.CharField(max_length=200)
    tala = models.CharField(max_length=200)
    worktype = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    position = models.IntegerField()
    length = models.CharField(max_length=10)

    @property
    def fixed_length(self):
        return self.length.lower().replace("o", "0")

    def __unicode__(self):
        return self.name

class Relationship(models.Model):
    track = models.ForeignKey(Track)
    artist = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s - %s" % (self.artist, self.instrument)
