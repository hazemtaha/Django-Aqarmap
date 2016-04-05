from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import redirect
from properties.models import Properties
from properties.forms import PropertiesForm
from django.core.paginator import   Paginator ,EmptyPage, PageNotAnInteger
from django.template import loader
from django.contrib.auth.decorators import login_required

import urlparse
from django import template
from django.conf import settings


# Create your views here.

@login_required
def listProperties(request):
    # template = loader.get_template('listProperties.html')

    p = Properties.objects.filter(owner_id=request.user.id)
    paginator = Paginator(p,1)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      contacts = paginator.page(paginator.num_pages)


    return render(request, 'listProperties.html', {'contacts': contacts})


    #context = {'p': p}

    #return render(request, "listProperties.html", context)




@login_required
def EditProp(request, prop_id):
    properties = Properties.objects.get(id=prop_id)
    if request.method == 'GET':
        form = PropertiesForm(instance=properties)
    else:
        form = PropertiesForm(request.POST, instance=properties)
        form.save()

        return redirect('listings:listProperties')
    context = {'form': form}

    return render(request, "editProperties.html", context)


@login_required
def delete(request, prop_id):

    property = Properties.objects.get(id=prop_id)
    property.delete()
    return redirect('listings:listProperties')
