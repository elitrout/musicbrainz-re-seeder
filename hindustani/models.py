from django.db import models
import eyed3

class Release(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    mbid = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    who = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title

    @property
    def num_images(self):
        # first file
        fpath = self.track_set.all()[0].filename
        f = eyed3.load(fpath)
        images = f.tag.frame_set["APIC"]
        return range(len(images))

    def get_image(self, num):
        fpath = self.track_set.all()[0].filename
        f = eyed3.load(fpath)
        images = f.tag.frame_set["APIC"]
        return images[num].image_data

class Track(models.Model):
    release = models.ForeignKey(Release)
    name = models.CharField(max_length=200)
    position = models.IntegerField()
    length = models.CharField(max_length=10)
    filename = models.CharField(max_length=255)
    disc = models.IntegerField()

    @property
    def fixed_length(self):
        return self.length.lower().replace("o", "0")

    def __unicode__(self):
        return self.name

