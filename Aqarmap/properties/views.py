from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from django.core.exceptions import ValidationError

from .models import Properties, PropertiesPhotos

from django.template import loader

# import the forms here
from django.forms import inlineformset_factory, BaseInlineFormSet

from .forms import PropertiesForm, PropertiesFormSet
# Create your views here.
import urlparse
from django import template
from django.conf import settings

register = template.Library()
import re


def prop_forSale(request):

    try:
        property_info = Properties.objects.all()
        context = {'property_info': property_info, }
    except Properties.DoesNotExist:
        return HttpResponse("There is no property to show")

    template = loader.get_template('properties/forSale.html')
    return HttpResponse(template.render(context, request))


# going to another page with the id
def prop_details(request, property_id):
    prop_info = get_object_or_404(Properties, id=property_id)
    prop_photos = PropertiesPhotos.objects.filter(prop_id=property_id)
    return render(request, 'properties/propDetails.html', {'prop_info': prop_info, 'value': property_id, 'prop_photos': prop_photos})


# def addProperty(request, addProperty_id):
def addProperty(request):
    # creating Form View
    # check first for the method if its post or get
    if request.method == "POST":
        # we will construct the form with it's data if it's a POST
        form = PropertiesForm(request.POST)

        # then check if the form is valid
        if form.is_valid():
            # process the data in the form.cleaned_data to return all the data
            # then accessing it
            values = form.cleaned_data
            title = values['title']
            properties = form.save(commit=False)

            prop_form_set = PropertiesFormSet(
                request.POST, request.FILES, instance=properties)

            if prop_form_set.is_valid():
                properties.save()
                prop_form_set.save()
                return HttpResponse("<h1 style=color:red>'" + title + "'has been saved into Property,Thank you!</h1>")
        else:
            prop_form_set = PropertiesFormSet(
                request.POST or None, instance=Properties())
            return HttpResponse("something went wrong")
    else:
        form = PropertiesForm()
        prop_form_set = PropertiesFormSet(
            request.POST or None, instance=Properties())

    template = loader.get_template('properties/addProperty.html')
    context = {'form': form, 'prop_form_set': prop_form_set, }
    return HttpResponse(template.render(context, request))
