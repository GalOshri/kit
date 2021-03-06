from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User
from reminder.models import FriendProfile, Event

def base(request):
	user = request.user
	context = { }
	return render(request, 'base.html', context)

def index(request):
	user = request.user
	# get only the friends and events of the user
	if user.is_authenticated():
		friend_list = user.owns.all
		event_list = user.asked.all
	else:
		friend_list = []
		event_list = []

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
	friend = FriendProfile(friend=request.user, firstName=request.POST['first_name'], lastName=request.POST['last_name'])
	friend.save()
	return HttpResponseRedirect('/')
	
def add_event_add(request):
	event = Event(owner=request.user,  
	name=request.POST['name'], 
	frequency=request.POST['frequency'], 
	time=request.POST['time'], 
	emailReminder=request.POST['emailReminder'], 
	text=request.POST['text'])
	event.save()
	event.participants.add(FriendProfile.objects.all()[0])
	event.save()
	return HttpResponseRedirect('/')
	
def friend_profile(request):
	context = {}
	return render(request, 'reminder/friend_profile.html', context)
	
def add_user(request):
	context = { }
	return render(request, 'registration/add_user.html', context)
	
def add_user_add(request):
	newUser = User.objects.create_user(request.POST['uname'],request.POST['email'], request.POST['pwd'])
	newUser.last_name = request.POST['last_name']
	newUser.first_name = request.POST['first_name']
	
	newUser.save()
	
	#add to UserProfiles
	addUserProf = newUser
	addUserProf.save()
	
	return HttpResponseRedirect('/')