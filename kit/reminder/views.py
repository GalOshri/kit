from django.shortcuts import render

from reminder.models import FriendProfile

def index(request):
	friend_list = FriendProfile.objects.all
	context = { 'friend_list' : friend_list }
	return render(request, 'reminder/index.html', context)
	
def add_friend(request):
	context = { }
	return render(request, 'reminder/add_friend.html', context)
	
def add_event(request):
	context = { }
	return render(request, 'reminder/add_event.html', context)