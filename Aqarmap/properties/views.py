from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,Http404

from .models import Properties

from django.template import loader

#import the forms here

from .forms import PropertiesForm
# Create your views here.

def index(request):
	return HttpResponse("Hello from my application")
#going to another page with the id
def details(request, prop_id):
	try:
		return HttpResponse("These are some details about property_id %s." % prop_id)		
	except:
		raise Http404("details dosen't exist anymore")


#add another view as a test
def addProperty(request, addProperty_id):
	#creating Form View
	#check first for the method if its post or get
	if request.method == "POST":
		#we will construct the form with it's data if it's a POST
		form = PropertiesForm(request.POST)
		#then check if the form is valid
		if form.is_valid():
			# process the data in the form.cleaned_data to return all the data then accessing it
			values = form.cleaned_data
			title = values['title']
			properties = form.save()
			properties.save()
			return HttpResponse("<h1 style=color:red>'"+title+"'has been saved into Property,Thank you!</h1>")
		else:
			return HttpResponse("something went wrong")
	else:	
		form = PropertiesForm()
	
	template = loader.get_template('properties/index.html')
	context = {'form': form,}
	return HttpResponse(template.render(context, request))