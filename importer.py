#!/bin/python

import csv
import sys
from itertools import izip

from mbimport import settings
from django.core.management import setup_environ
setup_environ(settings)

from carnatic.models import *

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def make_album(tracks):
    one = tracks[0]
    print "%s - %s" % (one[0], one[7])
    r = Release(title=one[0], albumid=one[1], artist=one[7])
    r.save()
    for i, t in enumerate(tracks, 1):
        tk = Track(release=r, name=t[2], raga=t[4], tala=t[5], worktype=t[3],
                    composer=t[6], position=i, length=t[18])
        tk.save()
        rels = t[8:18]
        for person, instr in pairwise(rels):
            if instr != '':
                rel = Relationship(track=tk, artist=person, instrument=instr)
                rel.save()

def main(fname):
    chandle = csv.reader(open(fname))
    lines = []
    albums = []
    tracks = []
    for c in chandle:
        if c[3] == 'Download Album':
            if len(tracks):
                albums.append(tracks)
            tracks = []
        else:
            tracks.append(c)
    # last one
    albums.append(tracks)
    for a in albums:
        make_album(a)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: importer.py <csvfile>"
    else:
        main(sys.argv[1])
