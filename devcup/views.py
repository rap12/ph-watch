from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Office

def home(request):
	return render_to_response ('index.html', {
	}, context_instance = RequestContext(request))
	
def view_map(request):
	office = (Office.objects.all() and Office.objects.all()[0]) or { "map": { show: "No maps defined" } }
	print office.x()
	print office.y()
	return render_to_response ('devcup/view_map.html', {
		'office': office
	}, context_instance = RequestContext(request))