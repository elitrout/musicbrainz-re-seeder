from django.db import models

class Release(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    catno = models.CharField(max_length=200)
    reldate = models.CharField(max_length=200)
    recdate = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Track(models.Model):
    release = models.ForeignKey(Release)
    name = models.CharField(max_length=200)
    position = models.IntegerField()
    disc = models.IntegerField()

    def __unicode__(self):
        return self.name

