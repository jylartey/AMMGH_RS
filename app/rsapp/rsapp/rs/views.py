from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def index(request):
	print("correct")
	context = {
		'message': 'Hello, Django!',
	}
	return render(request, 'index.html', context)

