from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse
from math import ceil

from store.models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'store/index.html', params)






def about(request):
    return render(request, "store/about.html")








#
# def contact(request):
#     return HttpResponse("You are at contact page")
#
#
#
#
#
# def tracker(request):
#     return HttpResponse("You are at tracker page")
#
#
#
#
#
# def search(request):
#     return HttpResponse("You are at search page")
#
#
#
#
#
# def productView(request):
#     return HttpResponse("You are at product view page")
#
#
#
#
#
# def checkout(request):
#     return render(request, "store/index.html")
#
