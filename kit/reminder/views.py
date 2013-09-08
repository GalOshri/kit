from django.shortcuts import render



def index(request):
	template = loader.get_template('reminder/index.html')
	context = { }
	return render(request, 'polls/index.html', context)
	
	