#!/bin/python

from mbimport import settings
from django.core.management import setup_environ
setup_environ(settings)

import sys
import os
import eyed3
import logging
logging.basicConfig(level=logging.INFO)

from hindustani.models import *

def load_single(dirname, files):
    print "Dir", dirname
    relname = ""
    artname = ""
    tags = []
    for one in files:
        if one.endswith("mp3"):
            f = eyed3.load(os.path.join(dirname, one))
            tags.append(f)
    print tags

    releases = [t.tag.album for t in tags]
    artists = [t.tag.artist for t in tags]

    if len(set(releases)) > 1:
        logging.WARN("Found more than 1 release name")
    if len(set(artists)) > 1:
        logging.WARN("Found more than 1 artist name")

    r = releases[0]
    a = artists[0]
    y = str(tags[0].tag.recording_date)
    rel = Release(title=r, artist=a, year=y)
    rel.save()
    for tr in sorted(tags, key=lambda tg: int(tg.tag.track_num[0])):
        track = Track(release=rel, name=tr.tag.title, position=tr.tag.track_num[0], length=tr.info.time_secs, filename=tr.path)
        if "/Ajay/" in tr.path:
            rel.who = "Ajay"
        else:
            rel.who = "Sankalp"
        track.save()
    rel.save()

def load(dirname):
    for (p, dirs, f) in os.walk(dirname):
        if len(f) > 0:
            load_single(p, f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: %s <dir>" % sys.argv[0]
    else:
        load(sys.argv[1])
