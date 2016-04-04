from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import redirect
from properties.models import Properties
from properties.forms import PropertiesForm
from django.template import loader

import urlparse
from django import template
from django.conf import settings


# Create your views here.


def listProperties(request):
    # template = loader.get_template('listProperties.html')

    p = Properties.objects.filter(owner_id=request.user.id)
    context = {'p': p}
    return render(request, "listProperties.html", context)


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

