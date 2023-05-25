from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="StoreHome"),
    path('about', views.about, name="About"),
    # path('contact', views.contact, name="Contact"),
    # path('tracker', views.tracker, name="Tracker"),
    # path('search', views.search, name="Search"),
    # path('productview', views.productView, name="productView"),
    # path('checkout', views.checkout, name="Checkout"),
]
