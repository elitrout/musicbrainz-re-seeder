# Create your views here.

from django.http import HttpResponse

from models import *
from django.template import Context, loader
from django.core.context_processors import csrf

import eyed3
import os

def home(request):
    releases = Release.objects.filter(done=False)
    template = loader.get_template('mbimport/index.html')
    context = Context({
        'releases': releases,
    })
    return HttpResponse(template.render(context))

def image(request, releaseid):
    release = Release.objects.get(albumid=releaseid)
    file_loc = "/home/alastair/CHARSUR_KUTCHERI"
    d = os.path.join(file_loc, release.artist, release.title)
    files = os.listdir(d)
    one = files[0]
    f = eyed3.load(os.path.join(d, one))
    img = f.tag.images.get(u"")
    resp = HttpResponse(img.image_data, "image/jpeg")

    return resp

def detail(request, releaseid):
    release = Release.objects.get(albumid=releaseid)
    if request.method == "POST":
        release.mbid = request.POST["releaseid"]
        release.save()
    template = loader.get_template('mbimport/detail.html')
    context = Context({
        'release': release,
        'rels': release.track_set.all()[0].relationship_set.all()
    })
    context.update(csrf(request))
    return HttpResponse(template.render(context))
