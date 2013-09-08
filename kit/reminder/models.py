from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	
	# associated with one user
    
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.user.first_name

#------------------------------------------

class FriendProfile(models.Model):

	friend = models.ForeignKey(User, related_name='owns')
	firstName = models.CharField(max_length=40)
	lastName = models.CharField(max_length=40)
	blurb = models.CharField(max_length=140, blank=True)
	storyNotes = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.firstName
	
class Event(models.Model):

	owner = models.ForeignKey(User, related_name='asked')
	participants = models.ManyToManyField('FriendProfile')
	eventName = models.CharField(max_length=40)
	
	#Frequency Categories
	WEEKLY = 'WE'
	MONTHLY = 'MO'
	BIWEEKLY = 'BI'
	YEARLY = 'YE'
	FREQUENCY_CHOICES = (
		(WEEKLY, 'Weekly'),
		(MONTHLY, 'Monthly'),
		(BIWEEKLY, 'Every other week'),
		(YEARLY, 'Yearly'),
	)
	frequency = models.CharField(max_length=2, choices=FREQUENCY_CHOICES, default=MONTHLY)
	time = models.TimeField()
	
	emailReminder = models.BooleanField()
	
	text = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.eventName