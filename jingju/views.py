from models import Release, Track
from django.shortcuts import render

import os

def home(request):
    releases = Release.objects.all()
    context = {"releases": releases}
    return render(request, 'jingju/index.html', context)


def detail(request, releaseid):
    release = Release.objects.get(id=releaseid)
    tracks = release.track_set.order_by('disc', 'position').all()
    max_disc = max([t.disc for t in tracks])

    context = {"release": release, "tracks": tracks, 'numdiscs': range(max_disc)}
    return render(request, "jingju/detail.html", context)
