from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def saverestaurant(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    #print(id + "->" + type + "->" + value)
    cursor = connection.cursor()
    if type == 'name':
        sql = "UPDATE RESTAURANT SET NAME = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'location':
        sql = "UPDATE RESTAURANT SET LOCATION_ID = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'phone':
        sql = "UPDATE RESTAURANT SET PHONE_NO = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'email':
        sql = "UPDATE RESTAURANT SET EMAIL = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'opening':
        sql = "UPDATE RESTAURANT SET OPENING = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'closing':
        sql = "UPDATE RESTAURANT SET CLOSING = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'image':
        sql = "UPDATE RESTAURANT SET IMAGE = '{}' WHERE RESTAURANT_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    cursor.close()
    return JsonResponse({"success":"Updated"})

@csrf_exempt
def addnewrestaurant(request):
    id=request.POST.get('id','')
    name=request.POST.get('name','')
    location=request.POST.get('location','')
    phone=request.POST.get('phone','')
    email=request.POST.get('email','')
    opening=request.POST.get('opening','')
    closing=request.POST.get('closing','')
    image=request.POST.get('image','')
    cursor = connection.cursor()
    sql = "INSERT INTO RESTAURANT(RESTAURANT_ID,NAME,LOCATION_ID,PHONE_NO,EMAIL,OPENING,CLOSING,IMAGE) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(id,name,location,phone,email,opening,closing,image)
    #print(sql)
    try:
        cursor.execute(sql)
        return JsonResponse({"success":"Updated"})
    except Exception as e:
        return JsonResponse({"failure":"DatabaseError"})
