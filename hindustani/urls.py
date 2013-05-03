from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'hindustani.views.home', name='h-home'),
    url(r'^(?P<releaseid>[0-9]+)$', 'hindustani.views.detail', name='h-detail'),
    url(r'^(?P<releaseid>[0-9]+)/image/(?P<num>[0-9]+)$', 'hindustani.views.image', name='h-image')
    )
