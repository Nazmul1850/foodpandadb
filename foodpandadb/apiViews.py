from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import foodpandadb.views as food_view


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

@csrf_exempt
def foodcall(request):
    res_id = request.POST.get('res_id','')
    if res_id == '':
        return JsonResponse({"failure":"nothing"})
    else:
        request.session['res_id'] = str(res_id)
        return JsonResponse({"success":"Updated"})

@csrf_exempt
def addnewfood(request):
    res_id = request.POST.get('res_id','')
    name = request.POST.get('name','')
    cuisine = request.POST.get('cuisine','')
    price = request.POST.get('price','')
    avl = request.POST.get('avl','')
    print(res_id + name + cuisine + price + avl)
    cursor = connection.cursor()
    sql = "SELECT COUNT(*) FROM FOOD"
    cursor.execute(sql)
    result = cursor.fetchall()
    count_id = result[0][0] + 1
    #print(count_id)
    sql = "INSERT INTO FOOD VALUES ('{}','{}','{}','{}','{}','{}')".format(count_id,name,cuisine,price,avl,res_id)
    print(sql)
    try:
        cursor.execute(sql)
        return JsonResponse({"success":"Updated"})
    except Exception as e:
        return JsonResponse({"failure":"DatabaseError"})

@csrf_exempt
def savefood(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    print(id + "->" + type + "->" + value)
    cursor = connection.cursor()
    if type == 'name':
        sql = "UPDATE FOOD SET NAME = '{}' WHERE FOOD_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'cuisine':
        sql = "UPDATE FOOD SET CUISINE = '{}' WHERE FOOD_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'price':
        sql = "UPDATE FOOD SET PRICE = '{}' WHERE FOOD_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'avl':
        sql = "UPDATE FOOD SET AVAILABILITY = '{}' WHERE FOOD_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    return JsonResponse({"success":"Nothing"})
