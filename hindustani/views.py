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

def image(request, releaseid):
    release = Release.objects.get(id=releaseid)
    track = release.track_set.all()[0]
    file_loc = track.filename
    f = eyed3.load(file_loc)
    images = f.tag.frame_set["APIC"]
    fronts = [i for i in images if i.picture_type == ImageFrame.FRONT_COVER]
    img = fronts[0]
    resp = HttpResponse(img.image_data, "image/jpeg")

    return resp

def detail(request, releaseid):
    release = Release.objects.get(id=releaseid)
    if request.method == "POST":
        release.mbid = request.POST["releaseid"]
        release.save()
    template = loader.get_template('hindustani/detail.html')
    context = Context({
        'release': release
    })
    context.update(csrf(request))
    return HttpResponse(template.render(context))
