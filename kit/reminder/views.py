from django.shortcuts import render

def index(request):
	context = { }
	return render(request, 'reminder/index.html', context)
	
def add_friend(request):
	context = { }
	return render(request, 'reminder/add_friend.html', context)
	
def add_event(request):
	context = { }
	return render(request, 'reminder/add_event.html', context)