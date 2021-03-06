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
        loc = value.split(',')
        sql = "SELECT LOCATION_ID FROM LOCATION WHERE LONGITUDE = '{}' AND LATITUDE = '{}'".format(loc[0],loc[1])
        cursor.execute(sql)
        result = cursor.fetchall()
        l_id = 0
        for r in result:
            l_id = r[0]
        if l_id == 0:
            sql ="SELECT COUNT(*) FROM LOCATION"
            cursor.execute(sql)
            res = cursor.fetchall()
            count_id = 0
            for r in res:
                count_id = r[0] + 1
            sql = "INSERT INTO LOCATION (LOCATION_ID,LONGITUDE,LATITUDE) VALUES ('{}','{}','{}')".format(count_id,loc[0],loc[1])
            cursor.execute(sql)
            sql = "UPDATE RESTAURANT SET LOCATION_ID = '{}' WHERE RESTAURANT_ID = '{}'".format(count_id,id)
            cursor.execute(sql)
            return JsonResponse({"success":"NewUpdated"})
        else:
            sql = "UPDATE RESTAURANT SET LOCATION_ID = '{}' WHERE RESTAURANT_ID = '{}'".format(l_id,id)
            cursor.execute(sql)
            return JsonResponse({"success":"PreUpdated"})
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
    if request.method == 'POST':
            id=request.POST.get('id','')
            name=request.POST.get('name','')
            location=request.POST.get('location','')
            phone=request.POST.get('phone','')
            email=request.POST.get('email','')
            opening=request.POST.get('opening','')
            closing=request.POST.get('closing','')
            image=request.POST.get('image','')
            cursor = connection.cursor()
            loc = location.split(',')
            sql = "SELECT LOCATION_ID FROM LOCATION WHERE LONGITUDE = '{}' AND LATITUDE = '{}'".format(loc[0],loc[1])
            cursor.execute(sql)
            result = cursor.fetchall()
            l_id = 0
            for r in result:
                l_id = r[0]
            if l_id == 0:
                sql ="SELECT COUNT(*) FROM LOCATION"
                cursor.execute(sql)
                res = cursor.fetchall()
                count_id = 0
                for r in res:
                    count_id = r[0] + 1
                sql = "INSERT INTO LOCATION (LOCATION_ID,LONGITUDE,LATITUDE) VALUES ('{}','{}','{}')".format(count_id,loc[0],loc[1])
                cursor.execute(sql)
                sqli = "INSERT INTO RESTAURANT(RESTAURANT_ID,NAME,LOCATION_ID,PHONE_NO,EMAIL,OPENING,CLOSING,IMAGE) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(id,name,count_id,phone,email,opening,closing,image)
            else:
                sqli = "INSERT INTO RESTAURANT(RESTAURANT_ID,NAME,LOCATION_ID,PHONE_NO,EMAIL,OPENING,CLOSING,IMAGE) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(id,name,l_id,phone,email,opening,closing,image)
            try:
                cursor.execute(sqli)
                return JsonResponse({"success":"Updated"})
            except Exception as e:
                return JsonResponse({"failure":"DatabaseError"})
    else:
        return JsonResponse({"failure":"GET"})


@csrf_exempt
def foodcall(request):
    res_id = request.POST.get('res_id','')
    if res_id == '':
        return JsonResponse({"failure":"nothing"})
    else:
        request.session['res_id'] = str(res_id)
        return JsonResponse({"success":"Updated"})
@csrf_exempt
def offercall(request):
    res_id = request.POST.get('res_id','')
    if res_id == '':
        return JsonResponse({"failure":"nothing"})
    else:
        request.session['res_id'] = str(res_id)
        return JsonResponse({"success":"Updated"})

@csrf_exempt
def personpromo(request):
    per_promo = request.POST.get('id','')
    print(per_promo)
    if per_promo == '':
        return JsonResponse({"failure":"nothing"})
    else:
        request.session['per_promo'] = str(per_promo)
        return JsonResponse({"success":"Updated"})

@csrf_exempt
def addnewfood(request):
    res_id = request.POST.get('res_id','')
    name = request.POST.get('name','')
    cuisine = request.POST.get('cuisine','')
    price = request.POST.get('price','')
    avl = request.POST.get('avl','')
    img = request.POST.get('img','')
    print(res_id + name + cuisine + price + avl)
    cursor = connection.cursor()
    sql = "SELECT COUNT(*) FROM FOOD"
    cursor.execute(sql)
    result = cursor.fetchall()
    count_id = result[0][0] + 1
    #print(count_id)
    sql = "INSERT INTO FOOD VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(count_id,name,cuisine,price,avl,res_id,price,img)
    print(sql)
    try:
        cursor.execute(sql)
        return JsonResponse({"success":"Updated"})
    except Exception as e:
        return JsonResponse({"failure":"DatabaseError"})

@csrf_exempt
def addnewoffer(request):
    discount_pct=request.POST.get('discount_pct','')
    max_discount=request.POST.get('max_discount','')
    expiry=request.POST.get('expiry','')
    res_id=request.POST.get('res_id','')
    start=request.POST.get('start','')
    cursor = connection.cursor()
    sql = "SELECT COUNT(*) FROM OFFERS"
    cursor.execute(sql)
    result = cursor.fetchall()
    count_id = result[0][0] + 1
    sql = "INSERT INTO OFFERS VALUES ('{}','{}','{}','{}','{}','{}')".format(count_id,discount_pct,max_discount,expiry,res_id,start)
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
        sql = "UPDATE FOOD SET AVAILABILTY = '{}' WHERE FOOD_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            print(e)
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'img':
        sql = "UPDATE FOOD SET IMAGE = '{}' WHERE FOOD_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            print(e)
            return JsonResponse({"failure":"DatabaseError"})
    return JsonResponse({"success":"Nothing"})


@csrf_exempt
def saveoffer(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    print(id + "->" + type + "->" + value)
    cursor = connection.cursor()
    if type == 'dpct':
        sql = "UPDATE OFFERS SET DISCOUNT_PCT = '{}' WHERE OFFER_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'maxd':
        sql = "UPDATE OFFERS SET MAX_DISCOUNT = '{}' WHERE OFFER_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'expd':
        sql = "UPDATE OFFERS SET EXPIRE_DATE = '{}' WHERE OFFER_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'res_id':
        sql = "UPDATE OFFERS SET RESTAURANT_ID = '{}' WHERE OFFER_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    if type == 'startd':
        sql = "UPDATE OFFERS SET START_DATE = '{}' WHERE OFFER_ID = '{}'".format(value,id)
        try:
            cursor.execute(sql)
            return JsonResponse({"success":"Updated"})
        except Exception as e:
            return JsonResponse({"failure":"DatabaseError"})
    return JsonResponse({"success":"Nothing"})

@csrf_exempt
def updateOffer(request):
    cursor = connection.cursor()
    cursor.callproc('OFFER_ENDS')
    return JsonResponse({"success":"Proc Called"})

@csrf_exempt
def updateprpmo(request):
    cursor = connection.cursor()
    cursor.callproc('PROMO_ENDS')
    return JsonResponse({"success":"Proc Called"})


@csrf_exempt
def addnewpromo(request):
    cursor = connection.cursor()
    code = request.POST.get('code','')
    discount = request.POST.get('discount','')
    start = request.POST.get('start','')
    end = request.POST.get('end','')
    status = request.POST.get('status','')
    print(code + status)
    sql = "INSERT INTO PROMO VALUES('{}','{}','{}','{}','{}')".format(code,discount,start,end,status)
    try:
        cursor.execute(sql)
        return JsonResponse({"success":"newPromo"})
    except Exception as e:
        return JsonResponse({"failure":"newPromonotAdded"})

@csrf_exempt
def addnewpersonpromo(request):
    code = request.POST.get('code','')
    id = request.POST.get('id','')
    cursor = connection.cursor()
    sql = "INSERT INTO CUSTOMER_PROMO VALUES('{}','{}')".format(code,id)
    print(code + "Called")
    try:
        print(code)
        print(id)
        print(sql)
        cursor.execute(sql)
        return JsonResponse({"success":"person promo Updated"})
    except Exception as e:
        return JsonResponse({"success":"promo dont exist"})
