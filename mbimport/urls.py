from django.conf.urls import patterns, include, url
import hindustani.urls
import carnatic.urls
import mbimport.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', mbimport.views.slash),
    url(r'^musicbrainz-seed/?$', mbimport.views.main, name='main'),
    url(r'^musicbrainz-seed/hindustani/', include(hindustani.urls.urlpatterns)),
    url(r'^musicbrainz-seed/carnatic/', include(carnatic.urls.urlpatterns)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
