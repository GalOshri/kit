from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User
from reminder.models import FriendProfile, Event

def index(request):
	friend_list = FriendProfile.objects.all
	event_list = Event.objects.all
	context = { 'friend_list' : friend_list, 'event_list' : event_list }
	return render(request, 'reminder/index.html', context)
	
def add_friend(request):
	context = { }
	return render(request, 'reminder/add_friend.html', context)
	
def add_event(request):
	possible_freq = []
	for freq in Event.FREQUENCY_CHOICES:
		possible_freq.append(freq[1])
	context = { 'possible_freq' : possible_freq }
	return render(request, 'reminder/add_event.html', context)
	
def add_friend_add(request):
	friend = FriendProfile(friend=User.objects.all()[0], firstName=request.POST['first_name'], lastName=request.POST['last_name'])
	friend.save()
	return HttpResponseRedirect('/')
	
def add_event_add(request):
	event = Event(owner=User.objects.all()[0],  
	name=request.POST['name'], 
	frequency=request.POST['frequency'], 
	time=request.POST['time'], 
	emailReminder=request.POST['reminder'], 
	text=request.POST['text'])
	event.save()
	event.participants.add(FriendProfile.objects.all()[0])
	event.save()
	return HttpResponseRedirect('/')