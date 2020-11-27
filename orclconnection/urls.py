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
import foodpandauth.views as auth_view
import homemodule.views as home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dbhome/',food_view.home,name="dbhome"),
    path('persons/', food_view.list_person, name='persons'),
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



# NOTE: Authenticate
  path('signupuser/', auth_view.signupuser, name='signupuser'),
  path('loginuser/',auth_view.loginuser, name='loginuser'),
  path('home/',auth_view.home,name='home'),
  path('logoutuser/',auth_view.logoutuser, name='logoutuser'),
  path('updateProfile/',auth_view.updateProfile, name='updateProfile'),

  # NOTE: homemodule
  path('',home_view.home, name="homelocation"),
  # path('res/',home_view.showRestaurant, name="showRestaurant"),
  path('confirmOrder/',home_view.confirmOrder,name='confirmOrder'),
  path('check/',home_view.check,name="check"),
]
