from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^musicbrainz-seed/?$', 'mbimport.views.home', name='home'),
    url(r'^musicbrainz-seed/(?P<releaseid>CDW[0-9]{3})$', 'mbimport.views.detail', name='detail'),
    url(r'^musicbrainz-seed/(?P<releaseid>CDW[0-9]{3})/image$', 'mbimport.views.image', name='image'),
    # url(r'^mbimport/', include('mbimport.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
