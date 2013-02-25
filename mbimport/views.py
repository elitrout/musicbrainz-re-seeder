from django.template import Context, loader

from django.shortcuts import render_to_response
from django.shortcuts import redirect

def slash(request):
    return redirect('main')

def main(request):
    return render_to_response('main.html')
