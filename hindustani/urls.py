from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'mbimport.views.home', name='home'),
    url(r'^/(?P<releaseid>CDW[0-9]{3})$', 'hindustani.views.detail', name='detail'),
    url(r'^/(?P<releaseid>CDW[0-9]{3})/image$', 'hindustani.views.image', name='image')
    )
