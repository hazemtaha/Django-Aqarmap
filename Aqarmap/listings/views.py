from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, Http404

from properties.models import Properties

from django.template import loader

import urlparse
from django import template
from django.conf import settings

# Create your views here.


def listProperties(request):
	#template = loader.get_template('listProperties.html')
	
	p = Properties.objects.filter(owner_id = request.user.id)
	context = {'p' : p}
	return render(request , "listProperties.html" , context)


def EditProp(request):

	p = Properties.objects.filter(owner_id = request.user.id)
	context = {'p' : p}
	return render (request , "editProperties.html" , context)