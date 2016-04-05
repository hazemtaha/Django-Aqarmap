from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from search.forms import SearchForm
from properties.models import Properties, PropertiesPhotos, PROPERTIES_TYPES
# Create your views here.


def main_search(request):
    form = SearchForm(request.GET or None)
    context = {
        "form": form,
    }
    return render(request, "search/main_search.html", context)


def search_results(request):
    if request.GET is not None:
        category = request.GET.get('category')
        city = request.GET.get('city')
        neighborhood = request.GET.get('neighborhood')
        prop_type = request.GET.get('prop_type')
        minimum_price = request.GET.get('minimum_price')
        maximum_price = request.GET.get('maximum_price')
        results = Properties.objects.filter(category=category, city=city or None,
                                            neighborhood=neighborhood or None, prop_type=prop_type or None,
                                            price__range=(minimum_price, maximum_price))

        # this will get all properties that have an image
        properties = PropertiesPhotos.objects.filter(
            prop__in=results).select_related('prop')
        paginator = Paginator(properties, 25)
        page = request.GET.get('page')
        try:
            props = paginator.page(page)
        except PageNotAnInteger:
            props = paginator.page(1)
        except EmptyPage:
            props = paginator.page(paginator.num_pages)
        sort = request.GET.get('sort', 'prop.created')
        context = {
            "results": props,
            "sort": sort,
        }
        return render(request, "search/results.html", context)


@login_required
def property_compare(request, first_prop, second_prop):
    results = Properties.objects.filter(Q(id=first_prop) | Q(id=second_prop))
    # this will get all properties that have an image
    properties = PropertiesPhotos.objects.filter(
        prop__in=results).select_related('prop')
    print(properties)
    context = {
        "results": properties,
    }
    return render(request, "search/compare.html", context)
