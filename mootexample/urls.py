import os

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'mootexample.views.forum', name='forum'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^avatar/', include('avatar.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
)

path = os.path.join(os.path.dirname(__file__), "user-uploads")
urlpatterns += url(r'^user-uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path}),

