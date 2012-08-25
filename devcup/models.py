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
	offices = models.ManyToManyField('Office', null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)
	contractor = models.CharField(max_length=100, null=True, blank=True)
	usercontributed = models.IntegerField(null=True, blank=True) # 1 - user contributed , 0 govt - contributed
	budget = models.FloatField(null=True, blank=True)
	progress = models.IntegerField(null=True, blank=True)
	like = models.IntegerField(null=True, blank=True)
	dislike = models.IntegerField(null=True, blank=True)
	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)
	address = GoogleMapsField(default="{ coordinates: [14.6001, 120.9843], zoom: 10, size: [400, 200] }")
	
	def __unicode__(self):
		return self.title
		
	def x(self):
		return self.address.coordinates[0]
		
	def y(self):
		return self.address.coordinates[1]		
admin.site.register(Project)


class Comment(models.Model):
	project = models.ForeignKey('Project')
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=2000)

	
admin.site.register(Comment)
