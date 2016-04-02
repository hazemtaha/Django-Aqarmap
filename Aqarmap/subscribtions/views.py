from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,Http404
from .models import Subscribtions
from subscribtions.forms import SubscribtionsForm
from django.template import loader
#def subscribtions(request):
	

def subscribtions(request):
    form = SubscribtionsForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, "subscribtion.html", context)

def add_subscribtion(request):
	if request.method == "GET":
        # we will construct the form with it's data if it's a POST
		form = SubscribtionsForm(request.POST)

        # then check if the form is valid
		if form.is_valid():
            # process the data in the form.cleaned_data to return all the data
            # then accessing it
			values = form.cleaned_data
			#title = values['title']
			sub = Subscribtions(city=values['city'],neighborhood=values['neighborhood'],property_type=values['property_type'],property_categories=values['property_categories'],min_price=values['min_price'],max_price=values['max_price'],status=values['status'],user_id=1)
			#subscribtions = form.save(commit=False)
			sub.save()
			return HttpResponse("<h1 style=color:red>'" + values['property_type'] + "'has been saved into Property,Thank you!</h1>")
	else:
		form = SubscribtionsForm()
	template = loader.get_template('subscribtion.html')
	context = {'form': form, }
	return HttpResponse(template.render(context, request))