from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.humanize.templatetags.humanize import intcomma
from models import Office, Project
from forms import ProjectForm

from gmapi import maps

from widgets import GoogleMap

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':'100%', 'height':'100%'}))

def home(request):
	projects = Project.objects.filter(usercontributed=1)
	
	gmap = maps.Map(opts = {
		'center': maps.LatLng(14, 121),
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 10,
		'mapTypeControlOptions': {
			 'style': maps.MapTypeControlStyle.DROPDOWN_MENU
		},
	})
	
	form = MapForm(initial={'map': gmap})
	
	print projects
	
	for project in projects:
		marker = maps.Marker(opts = {
			'map': gmap,
			'position': maps.LatLng(project.x(), project.y()),
		})
		maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
		maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
		info = maps.InfoWindow({
			'content': '<h3>%s</h3><br><h4>Budget: <h4>P%s<br><h4>Start Date: <h4>%s<br><h4>End Date: <h4>%s<br>' % (project.title, intcomma(project.budget), project.start_date.strftime('%B %d %Y'), project.end_date.strftime('%B %d %Y')),
			'disableAutoPan': True
		})
		info.open(gmap, marker)
	return render_to_response ('index.html', {
		'gmap': form, 'projects': projects, 
	}, context_instance = RequestContext(request))
	
	
def add_project(request):
	if request.method == 'GET':
		form = ProjectForm()
	elif request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
	return render_to_response ('devcup/add_project.html', {
		'form': form,
	}, context_instance = RequestContext(request))


def showGovernmentProjects(request):
	projects = Project.objects.filter(usercontributed=0)
	
	gmap = maps.Map(opts = {
		'center': maps.LatLng(14, 121),
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 10,
		'mapTypeControlOptions': {
			 'style': maps.MapTypeControlStyle.DROPDOWN_MENU
		},
	})
	
	form = MapForm(initial={'map': gmap})
	
	for project in projects:
		marker = maps.Marker(opts = {
			'map': gmap,
			'position': maps.LatLng(project.x(), project.y()),
		})
		maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
		maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
		info = maps.InfoWindow({
			'content': '<h3>%s</h3><br><h4>Budget: <h4>P%s<br><h4>Start Date: <h4>%s<br><h4>End Date: <h4>%s<br>' % (project.title, intcomma(project.budget), project.start_date.strftime('%B %d %Y'), project.end_date.strftime('%B %d %Y')),
			'disableAutoPan': True
		})
		info.open(gmap, marker)
	return render_to_response ('index.html', {
		'gmap': form, 'projects': projects, 
	}, context_instance = RequestContext(request))	
