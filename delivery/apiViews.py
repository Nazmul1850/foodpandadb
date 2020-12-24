from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import delivery.views as deli_view




@csrf_exempt
def completeDelivery(request):
    cursor = connection.cursor()
    id=request.POST.get('id','')
    d_id = request.session['Delivery_id']
    print(d_id)
    sql = "UPDATE ORDERS SET STATUS = 'DELIVERED', DELIVERY_TIME = SYSDATE, DELIVERY_MAN_ID = '{}' WHERE ORDER_ID = {}".format(d_id,id)
    print(sql)
    try:
        cursor.execute(sql)
        return JsonResponse({"success":"Completed"})
    except Exception as e:
        print(sql)
        return JsonResponse({"failure":"DatabaseError"})
