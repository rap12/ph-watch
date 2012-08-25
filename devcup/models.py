from gmapsfield.fields import GoogleMapsField
from wdwebapp.fields import PercentField

from django.contrib import admin
from django.db import models

class Office(models.Model):
	name = models.CharField(max_length=100)
	contact_no = models.IntegerField()
	email = models.EmailField()
	head = models.CharField(max_length=100)
	address = GoogleMapsField()
	
	def __unicode__(self):
		return self.name
	
admin.site.register(Office)

class Project(models.Model):
	title = models.CharField(max_length=100)
	office = models.ForeignKey('Office')
	contractor = models.CharField(max_length=100)
	budget = models.FloatField()
	progress = PercentField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	address = GoogleMapsField()
	
	def __unicode__(self):
		return self.title
	
admin.site.register(Project)