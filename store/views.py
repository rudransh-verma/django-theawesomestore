from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse
from math import ceil

from store.models import Product
# Create your views here.

def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4)) 
        allProds.append([prod, range(1, nSlides), nSlides])

        
    params = {
        'allProds': allProds
    }


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
