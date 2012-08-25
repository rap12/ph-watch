from gmapsfield.fields import GoogleMapsField
from wdwebapp.fields import PercentField


from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class Office(models.Model):
	name = models.CharField(max_length=100)
	initials = models.CharField(max_length=10)
	contact_no = models.CharField(max_length=20)
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
	offices = models.ManyToManyField('Office')
	contractor = models.CharField(max_length=100)
	usercontributed = models.IntegerField() # 1 - user contributed , 0 govt - contributed
	budget = models.FloatField()
	progress = models.IntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	address = GoogleMapsField(default="{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }")
	
	def __unicode__(self):
		return self.title
	
admin.site.register(Project)


class Comment(models.Model):
	project = models.ForeignKey('Project')
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=2000)

	
admin.site.register(Comment)
