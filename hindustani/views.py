from django.http import HttpResponse
from models import *
from django.template import Context, loader
from django.core.context_processors import csrf
from eyed3.id3.frames import ImageFrame

import eyed3
import os

def home(request):
    ajay = Release.objects.filter(done=False, who="Ajay")
    sankalp = Release.objects.filter(done=False, who="Sankalp")
    template = loader.get_template('hindustani/index.html')
    context = Context({
        'ajay': ajay,
        'sankalp': sankalp
    })
    return HttpResponse(template.render(context))


def image(request, releaseid, num):
    release = Release.objects.get(id=releaseid)
    contents = release.get_image(int(num))
    resp = HttpResponse(contents, "image/jpeg")

    return resp

def detail(request, releaseid):
    release = Release.objects.get(id=releaseid)
    tracks = release.track_set.order_by('disc', 'position').all()
    max_disc = max([t.disc for t in tracks])

    if request.method == "POST":
        release.mbid = request.POST["releaseid"]
        release.save()
    template = loader.get_template('hindustani/detail.html')
    context = Context({
        'release': release,
        'tracks': tracks,
        'numdiscs': range(max_disc)
    })
    context.update(csrf(request))
    return HttpResponse(template.render(context))
