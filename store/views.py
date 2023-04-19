from django.shortcuts import render
from django.conf.urls.static import static
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "store/index.html")





def about(request):
    return HttpResponse("You are at about page")





def contact(request):
    return HttpResponse("You are at contact page")





def tracker(request):
    return HttpResponse("You are at tracker page")





def search(request):
    return HttpResponse("You are at search page")





def productView(request):
    return HttpResponse("You are at product view page")





def checkout(request):
    return render(request, "store/index.html")

