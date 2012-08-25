from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Office

from gmapi import maps
from gmapi.forms.widgets import GoogleMap

class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))

def home(request):
	return render_to_response ('index.html', {
	}, context_instance = RequestContext(request))
	
def view_map(request):
	offices = Office.objects.all()
	forms = []
	
	for office in offices:
		gmap = maps.Map(opts = {
			'center': maps.LatLng(office.x(), office.y()),
			'mapTypeId': maps.MapTypeId.ROADMAP,
			'zoom': 3,
			'mapTypeControlOptions': {
				 'style': maps.MapTypeControlStyle.DROPDOWN_MENU
			},
		})
		form = MapForm(initial={'map': gmap})
		forms.append(form)
	
	return render_to_response ('devcup/view_map.html', {
		'forms': forms,
	}, context_instance = RequestContext(request))