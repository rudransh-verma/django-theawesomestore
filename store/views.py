from math import ceil

from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse
from math import ceil

from store.models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n-4)/(n//4))
    # params = {
    #     'product': products,
    #     'no_of_slides': nSlides,
    #     'range': range(1, nSlides)
    # }

    allProds = [[products, range(1, len(products)), nSlides], [products, range(1, len(products)), nSlides]]
    params = {'allProds': allProds}

    return render(request, "store/index.html", params)


def about(request):
    return render(request, "store/about.html")
