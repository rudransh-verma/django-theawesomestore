from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse
from math import ceil

from store.models import Product
# Create your views here.
def index(request):
    var = Product.objects.all()
    n = len(var)
    nSlides = n//4 + ceil((n/4)-(n//4))
    dict = {
        'prodslides': nSlides,
        'prod': var,
    }
    return render(request, "store/index.html", dict)


def about(request):
    return render(request, "store/about.html")