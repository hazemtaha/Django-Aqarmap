from django.shortcuts import render
from .forms import SearchForm
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

        # properties = PropertiesPhotos.objects.all().select_related('prop')
        properties = PropertiesPhotos.objects.filter(
            prop__in=results).select_related('prop')
        context = {
            "results": properties,
        }
        return render(request, "search/results.html", context)
