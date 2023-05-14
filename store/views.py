from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse

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
<<<<<<< HEAD
    return render(request, "store/about.html")
<<<<<<< HEAD
<<<<<<< HEAD
=======
    return render(request, "store/about.html")
=======
>>>>>>> parent of 8879d95 (cwh-homepagelist)
=======
>>>>>>> parent of 8879d95 (cwh-homepagelist)

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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 8879d95 (cwh-homepagelist)
=======
>>>>>>> parent of 8879d95 (cwh-homepagelist)
=======
>>>>>>> parent of 8879d95 (cwh-homepagelist)
