from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import homemodule.views as home_view




@csrf_exempt
def completeOrder(request):
    print("Here")
    if 'order_id' in request.session:
        del request.session['order_id']
        return JsonResponse({"success":"Completed"})
    else:
        return JsonResponse({"failure":"something wrong"})
