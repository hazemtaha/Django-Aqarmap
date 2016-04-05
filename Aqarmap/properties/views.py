from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, Http404
from django.core.exceptions import ValidationError
from .models import Properties, PropertiesPhotos
from django.contrib.auth.decorators import login_required

from django.template import loader
# import the forms here
from django.forms import inlineformset_factory, BaseInlineFormSet
from .forms import PropertiesForm, PropertiesFormSet
# Create your views here.
import urlparse
from django import template
from django.conf import settings
#import things for paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




register = template.Library()
import re


@login_required
def prop_forSale(request):

    try:
        property_info = Properties.objects.filter(category='s')
        prop_photos = PropertiesPhotos.objects.filter(prop__in=property_info).select_related('prop')
            
        #Dealing with the paginators>>>>>>>>>>>>>>>>>>>>>>>
        paginator = Paginator(prop_photos, 3) # show 3 property per page
        page = request.GET.get('page')

        try: 
            props_pagin = paginator.page(page)
        except PageNotAnInteger:
            #if page is not int > deliver the first page only
            props_pagin = paginator.page(1)
        except EmptyPage:
            #if page is out of range (e.g), deliver last page of result
            props_pagin = paginator.page(paginator.num_pages)       


        #End of paginator>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        context = {'property_info': property_info,'prop_photos':prop_photos,'props_pagin':props_pagin,}
        

    except Properties.DoesNotExist:
        return HttpResponse("There is no property to show")


    template = loader.get_template('properties/forSale.html')
    return HttpResponse(template.render(context, request))


@login_required
def prop_forRent(request):

    try:
        property_info = Properties.objects.filter(category='r')
        prop_photos = PropertiesPhotos.objects.filter(prop__in=property_info).select_related('prop')
            
        #Dealing with the paginators>>>>>>>>>>>>>>>>>>>>>>>
        paginator = Paginator(prop_photos, 3) # show 3 property per page
        page = request.GET.get('page')

        try: 
            props_pagin = paginator.page(page)
        except PageNotAnInteger:
            #if page is not int > deliver the first page only
            props_pagin = paginator.page(1)
        except EmptyPage:
            #if page is out of range (e.g), deliver last page of result
            props_pagin = paginator.page(paginator.num_pages)       


        #End of paginator>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        context = {'property_info': property_info,'prop_photos':prop_photos,'props_pagin':props_pagin,}
        

    except Properties.DoesNotExist:
        return HttpResponse("There is no property to show")


    template = loader.get_template('properties/forRent.html')
    return HttpResponse(template.render(context, request))


@login_required
def list_u_prop(request):

    try:
        property_info = Properties.objects.all()
        prop_photos = PropertiesPhotos.objects.filter(prop__in=property_info).select_related('prop')
            
        #Dealing with the paginators>>>>>>>>>>>>>>>>>>>>>>>
        paginator = Paginator(prop_photos, 3) # show 3 property per page
        page = request.GET.get('page')

        try: 
            props_pagin = paginator.page(page)
        except PageNotAnInteger:
            #if page is not int > deliver the first page only
            props_pagin = paginator.page(1)
        except EmptyPage:
            #if page is out of range (e.g), deliver last page of result
            props_pagin = paginator.page(paginator.num_pages)       


        #End of paginator>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        context = {'property_info': property_info,'prop_photos':prop_photos,'props_pagin':props_pagin,}
        

    except Properties.DoesNotExist:
        return HttpResponse("There is no property to show")

    template = loader.get_template('properties/listProperties.html')
    return HttpResponse(template.render(context, request))


# going to another page with the id
@login_required
def prop_details(request, property_id):
    prop_info = get_object_or_404(Properties, id=property_id)
    prop_photos = PropertiesPhotos.objects.filter(prop_id=property_id)
    property_info = Properties.objects.all()
    prop_first = PropertiesPhotos.objects.filter(
        prop__in=property_info).select_related('prop').first()
    return render(request, 'properties/propDetails.html', {'prop_info': prop_info, 'value': property_id, 'prop_photos': prop_photos, 'prop_first': prop_first, })

# def addProperty(request, addProperty_id):


@login_required
def add_property(request):
    form = PropertiesForm(request.POST or None)
    if form.is_valid():
        properties = form.save(commit=False)
        prop_form_set = PropertiesFormSet(
            request.POST, request.FILES, instance=properties)

        if prop_form_set.is_valid():
            properties.owner = request.user
            properties.save()
            prop_form_set.save()
            return redirect('listings:listProperties')
        else:
            prop_form_set = PropertiesFormSet(
                request.POST or None, instance=Properties())
    else:
        prop_form_set = PropertiesFormSet()
    context = {'form': form, 'prop_form_set': prop_form_set, }
    return render(request, 'properties/addProperty.html', context)


# @login_required
# def addProperty(request):
#     # creating Form view
#     # check first for the method if its post or get
#     if request.method == "POST":
#         # we will construct the form with it's data if it's a POST
#         form = PropertiesForm(request.POST)

#         # then check if the form is valid
#         if form.is_valid():
#             # process the data in the form.cleaned_data to return all the data
#             # then accessing it
#             values = form.cleaned_data
#             title = values['title']
#             properties = form.save(commit=False)

#             prop_form_set = PropertiesFormSet(
#                 request.POST, request.FILES, instance=properties)

#             if prop_form_set.is_valid():
#                 properties.owner = request.user
#                 properties.save()
#                 prop_form_set.save()
#                 return redirect('listings:listProperties')
#         else:
#             prop_form_set = PropertiesFormSet(
#                 request.POST or None, instance=Properties())
#             return HttpResponse("something went wrong")
#     else:
#         form = PropertiesForm()
#         prop_form_set = PropertiesFormSet(
#             request.POST or None, instance=Properties())

#     template = loader.get_template('properties/addProperty.html')
#     context = {'form': form, 'prop_form_set': prop_form_set, }
#     return HttpResponse(template.render(context, request))
