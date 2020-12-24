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
import foodpandadb.apiViews as db_view
import foodpandauth.views as auth_view
import homemodule.views as home_view
import homemodule.apiViews as home_apiview
import delivery.views as deli_view
import delivery.apiViews as deli_apiview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodpandadmin/',food_view.foodpandadmin,name="foodpandadmin"),
    path('loginadmin/',food_view.loginadmin, name='loginadmin'),
    path('logoutadmin/',food_view.logoutadmin, name='logoutadmin'),

    path('saverestaurant/',db_view.saverestaurant, name="saverestaurant"),
    path('addnewrestaurant/',db_view.addnewrestaurant, name="addnewrestaurant"),
    path('foodcall/',db_view.foodcall, name="foodcall"),
    path('offercall/',db_view.offercall, name="offercall"),
    path('addnewfood/',db_view.addnewfood, name="addnewfood"),
    path('savefood/',db_view.savefood, name="savefood"),
    path('addnewoffer/',db_view.addnewoffer, name="addnewoffer"),
    path('saveoffer/',db_view.saveoffer, name="saveoffer"),
    path('updateOffer/',db_view.updateOffer, name="updateOffer"),
    path('completeDelivery/',deli_apiview.completeDelivery, name="completeDelivery"),
    path('addnewpromo/',db_view.addnewpromo, name="addnewpromo"),
    path('personpromo/',db_view.personpromo, name="personpromo"),
    path('addnewpersonpromo/',db_view.addnewpersonpromo, name="addnewpersonpromo"),
    path('updateprpmo/',db_view.updateprpmo, name='updateprpmo'),

    path('persons/', food_view.list_person, name='persons'),
    path('food/', food_view.food, name='food'),
    path('restaurant/', food_view.restaurant, name='restaurant'),
    path('locations/', food_view.locations, name='locations'),
    path('orders/', food_view.orders, name='orders'),
    path('promos/', food_view.promos, name='promos'),
    path('payments/', food_view.payments, name='payments'),
    path('offers/', food_view.offers, name='offers'),
    path('reviews/', food_view.reviews, name='reviews'),
    path('customer_promo/', food_view.customer_promo, name='customer_promo'),


    path('delivery/',deli_view.delivery,name='delivery'),
    path('logindelivery/',deli_view.logindelivery,name='logindelivery'),
    path('logoutdelivery/',deli_view.logoutdelivery,name='logoutdelivery'),
    path('updateDelivery/',deli_view.updateDelivery,name='updateDelivery'),
    path('signupDelivery/',deli_view.signupDelivery,name='signupDelivery'),


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
  path('myorders/',home_view.myorders,name="myorders"),
  path('receiveOrder/',home_view.receiveOrder,name="receiveOrder"),
   path('completeOrder/',home_apiview.completeOrder,name="completeOrder"),
   path('mycart/',home_view.mycart,name="mycart"),
   path('extra/',home_view.extra,name="extra"),
]
