from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Office, Project

from gmapi import maps
from gmapi.forms.widgets import GoogleMap

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':800, 'height':600}))

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
	
	for project in projects:
		marker = maps.Marker(opts = {
			'map': gmap,
			'position': maps.LatLng(project.x(), project.y()),
		})
		maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
		maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
		info = maps.InfoWindow({
			'content': 'Hello!',
			'disableAutoPan': True
		})
		info.open(gmap, marker)
	return render_to_response ('index.html', {
		'gmap': form, 'projects': projects, 
	}, context_instance = RequestContext(request))