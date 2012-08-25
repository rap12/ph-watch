from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^view_map/$', 'devcup.views.view_map', name='view_map'),
)