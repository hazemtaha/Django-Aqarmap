from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,Http404
from .models import Subscribtions
def subscribtions(request):
	return HttpResponse("hi")

def subForm(request):
	if request.method == "POST":
		sub = SubscribtionsForm(request.POST)
		if sub.is_valid():
			values = sub.save()
			values.save()
