from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def hello(request):
	return HttpResponse("Hello from my application")
