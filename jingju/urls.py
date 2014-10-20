from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'jingju.views.home', name='jhome'),
    url(r'^(?P<releaseid>[0-9]+)$', 'jingju.views.detail', name='jdetail'),
    )
