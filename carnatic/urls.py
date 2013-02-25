from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'carnatic.views.home', name='c-home'),
    url(r'^(?P<releaseid>CDW[0-9]{3})$', 'carnatic.views.detail', name='c-detail'),
    url(r'^(?P<releaseid>CDW[0-9]{3})/image$', 'carnatic.views.image', name='c-image')
    )
