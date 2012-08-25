from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^add_project/$', 'devcup.views.add_project', name='add_project'),
    url(r'^government_projects/$', 'devcup.views.showGovernmentProjects', name='show_government_projects'),
)