from gmapsfield.fields import GoogleMapsField
from wdwebapp.fields import PercentField

from django.contrib import admin
from django.db import models

from widgets import *

class Office(models.Model):
	name = models.CharField(max_length=100)
	contact_no = models.IntegerField()
	email = models.EmailField()
	head = models.CharField(max_length=100)
	address = GoogleMapsField(default="{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }")
	
	def __unicode__(self):
		return self.name
		
	def x(self):
		return self.address.coordinates[0]
		
	def y(self):
		return self.address.coordinates[1]
	
admin.site.register(Office)

class Project(models.Model):
	title = models.CharField(max_length=100)
	office = models.ForeignKey('Office')
	contractor = models.CharField(max_length=100)
	budget = models.FloatField()
	#progress = PercentField()
	progress = models.IntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	address = GoogleMapsField(default="{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }")
	
	def __unicode__(self):
		return self.title
	
admin.site.register(Project)