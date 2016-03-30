from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,Http404
from django.core.exceptions import ValidationError

from .models import Properties, PropertiesPhotos

from django.template import loader

#import the forms here
from django.forms import inlineformset_factory, BaseInlineFormSet

from .forms import PropertiesForm, PropertiesFormSet
# Create your views here.




def prop_forSale(request):

	try:
		property_info = Properties.objects.all()
		propPhoto_info = PropertiesPhotos.objects.all()

		context = {'property_info':property_info,'propPhoto_info':property_info,}
	except Properties.DoesNotExist:
		return HttpResponse("There is no property to show")

	template = loader.get_template('properties/forSale.html')
	return HttpResponse(template.render(context,request))




#going to another page with the id
def details(request, prop_id):
	try:
		return HttpResponse("These are some details about property_id %s." % prop_id)		
	except:
		raise Http404("details dosen't exist anymore")






#def addProperty(request, addProperty_id):
def addProperty(request):
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
			properties = form.save(commit=False)
			
			prop_form_set = PropertiesFormSet(request.POST,request.FILES, instance = properties)

			if prop_form_set.is_valid():
				properties.save()
				prop_form_set.save()
				return HttpResponse("<h1 style=color:red>'"+title+"'has been saved into Property,Thank you!</h1>")
		else:	
			prop_form_set = PropertiesFormSet(request.POST or None, instance = Properties())
			return HttpResponse("something went wrong")
	else:	
		form = PropertiesForm()
		prop_form_set = PropertiesFormSet(request.POST or None, instance = Properties())

	template = loader.get_template('properties/addProperty.html')
	context = {'form': form,'prop_form_set':prop_form_set,}
	return HttpResponse(template.render(context, request))



