from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,Http404
from .models import Subscribtions
from properties.models import Properties
from django.db.models import Q
from cities_light.models import City, Region
from subscribtions.forms import SubscribtionsForm
from django.template import loader
#def subscribtions(request):
	

def subscribtions(request):
	
    form = SubscribtionsForm(request.POST or None)
    subs = Subscribtions.objects.all()
    context = {
        "form": form,
        "subs": subs,
    }
    return render(request, "subscribtion.html", context)

def add_subscribtion(request):
	if request.method == "GET":
        # we will construct the form with it's data if it's a POST
		form = SubscribtionsForm(request.GET)

        # then check if the form is valid
		if form.is_valid():
            # process the data in the form.cleaned_data to return all the data
            # then accessing it
			values = form.cleaned_data
			#title = values['title']
			# cityId = values['city']
			# neighborhoodId = values['neighborhood']
			# cityObj = Region.objects.get(id=int(cityId))
			# neighborhoodObj = City.objects.get(id=int(neighborhoodId))

			sub = Subscribtions(property_type=values['property_type'],property_categories=values['property_categories'],
				min_price=values['min_price'],max_price=values['max_price'],
				city=values['city'], neighborhood= values['neighborhood'], user=request.user)
			#subscribtions = form.save(commit=False)
			sub.save()
			return redirect('subscribtions:subscribtions')
	else:
		form = SubscribtionsForm()
	template = loader.get_template('subscribtion.html')
	context = {'form': form, }
	return HttpResponse(template.render(context, request))

def active(request):
	sub_id = request.GET.get("sub_id")
	sub = Subscribtions.objects.get(pk=sub_id)
	if sub.status == False:
		sub.status = True
		sub.save()
	else:
		sub.status = False
		sub.save()	
	return redirect('subscribtions:subscribtions')

def delete_sub(request):
	sub_id = request.GET.get("sub_id")
	sub = Subscribtions.objects.get(pk=sub_id).delete()
	return redirect('subscribtions:subscribtions')

def sub_results(request):
	sub = Subscribtions.objects.filter(user_id=request.user)
	subs = []
	for subscribtion in sub:
		prop = Properties.objects.filter(city=subscribtion.city,neighborhood=subscribtion.neighborhood,category=subscribtion.property_categories,prop_type=subscribtion.property_type,price__range=(subscribtion.min_price,subscribtion.max_price))
		if prop in subs:
			continue
		else:	
			subs.append(prop)
	template = loader.get_template('results.html')
	context = {'subs':subs,}
	#print(subs[0].values('id'))
	return HttpResponse(template.render(context, request))