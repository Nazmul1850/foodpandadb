"""orclconnection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import foodpandadb.views as food_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',food_view.home),
    path('persons/', food_view.list_person, name='persons'),
    path('customers/', food_view.customers, name='customers'),
    path('delivery/', food_view.delivery, name='delivery'),
    path('locations/', food_view.locations, name='locations'),
    path('food/', food_view.food, name='food'),
    path('restaurant/', food_view.restaurant, name='restaurant'),
    path('orders/', food_view.orders, name='orders'),
    path('promos/', food_view.promos, name='promos'),
    path('payments/', food_view.payments, name='payments'),
    path('offers/', food_view.offers, name='offers'),
    path('reviews/', food_view.reviews, name='reviews'),
    path('customer_promo/', food_view.customer_promo, name='customer_promo'),
    path('orderd_items/', food_view.orderd_items, name='orderd_items'),
    path('menu/', food_view.menu, name='menu'),
]
