from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from array import array
import js2py
import time
import hashlib;

# Create your views here.
def home(request):
    if 'Person_id' in request.session:
        adress = {'ip':request.ipinfo.ip,
                  'latitude':request.ipinfo.latitude,
                  'longitude':request.ipinfo.longitude,
                  'region':request.ipinfo.region,
                  'postal':request.ipinfo.postal,
                  'city':request.ipinfo.city,
                  'country':request.ipinfo.country}
        if (request.method == 'GET'):
            cursor = connection.cursor()
            sql = "SELECT RESTAURANT_ID, NAME, PHONE_NO, OPENING, CLOSING, IMAGE, RATING FROM RESTAURANT WHERE RESTAURANT.LOCATION_ID IN ( SELECT LOCATION_ID FROM LOCATION WHERE ((LONGITUDE - "
            sql += str(request.ipinfo.longitude)
            sql += ")*1000 BETWEEN -5 AND 5) AND ((LATITUDE - "
            sql += str(request.ipinfo.latitude)
            sql += ")*1000 BETWEEN -5 AND 5) );"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            dict_result = []
            for r in result:
                id = r[0]
                name = r[1]
                phone = r[2]
                openning = r[3]
                closing = r[4]
                image = r[5]
                rat = r[6]
                row = {'id':id, 'name':name, 'phone':phone, 'openning':openning, 'closing':closing, 'image':image,'rat':rat}
                dict_result.append(row)
            return render(request,'homemodule/home.html',{'address':adress,'restaurant':dict_result})
        else:
            searchfilter = request.POST.get('res-filter')
            searchbox = request.POST.get('searchbox')
            res_name = request.POST.get('res_name')
            cursor = connection.cursor()
            if searchfilter and searchbox:
                search = ""
                price = 9999
                if searchfilter == 'price':
                    price = int(searchbox)
                else:
                    search = "%"
                    for c in searchbox:
                        search += c
                        search += '%'
                print(search)
                result = ""
                if searchfilter == 'restaurant':
                    result = cursor.callfunc('restaurant_ids', str , [search,'',price,'RESTAURANT'])
                    print(result)
                elif searchfilter == 'cuisine':
                    result = cursor.callfunc('restaurant_ids', str , ['',search,price,'CUISINE'])
                    print(result)
                else:
                    result = cursor.callfunc('restaurant_ids', str , ['','',price,'PRICE'])
                    print(result)
                sql = "SELECT RESTAURANT_ID, NAME, PHONE_NO, OPENING, CLOSING, IMAGE, RATING FROM RESTAURANT WHERE RESTAURANT_ID IN {} AND RESTAURANT.LOCATION_ID IN ( SELECT LOCATION_ID FROM LOCATION WHERE ((LONGITUDE - '{}')*1000 BETWEEN -5 AND 5) AND ((LATITUDE - '{}')*1000 BETWEEN -5 AND 5) )".format(result,request.ipinfo.longitude,request.ipinfo.latitude)
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.close()
                dict_result = []
                for r in result:
                    id = r[0]
                    name = r[1]
                    phone = r[2]
                    openning = r[3]
                    closing = r[4]
                    image = r[5]
                    rat = r[6]
                    row = {'id':id, 'name':name, 'phone':phone, 'openning':openning, 'closing':closing, 'image':image,'rat':rat}
                    dict_result.append(row)
                return render(request,'homemodule/home.html',{'address':adress,'restaurant':dict_result})
            else:
                if res_name:
                    res_property = {}
                    res_property= {'name':res_name,'image':'','rat':0,'offer':''}
                    cursor = connection.cursor()
                    sql = "SELECT FOOD_ID, NAME, CUISINE, PRICE, AVAILABILTY, OFFER_PRICE, IMAGE FROM FOOD WHERE RESTAURANT_ID = ( SELECT RESTAURANT_ID FROM RESTAURANT WHERE NAME = '"
                    sql += str(res_name)
                    sql += "')"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    dict_result = {}
                    for r in result:
                        id = r[0]
                        name = r[1]
                        cuisine = r[2]
                        price = r[3]
                        avl = r[4]
                        offer_price = r[5]
                        image = r[6]
                        if avl == 'y' or avl == 'Y':
                            if price == offer_price:
                                row = {'res_name':res_name, 'id':id, 'name':name,'cuisine':cuisine,'price':price,'avl':avl,'offer_price':offer_price,'status':0,'image':image}
                            else:
                                row = {'res_name':res_name, 'id':id, 'name':name,'cuisine':cuisine,'price':price,'avl':avl,'offer_price':offer_price,'status':1,'image':image}
                                res_property['offer'] = "present"
                        else:
                            continue;
                        try:
                            dict_result[cuisine].append(row)
                        except Exception as e:
                            dict_result[cuisine] = []
                            dict_result[cuisine].append(row)
                    #print(dict_result)
                    sql = "SELECT REV.ORDER_ID, REV.RATING, REV.DESCRIPTION FROM REVIEWS REV JOIN RESTAURANT RES ON (REV.RESTAURANT_ID = RES.RESTAURANT_ID) WHERE RES.NAME = '{}'".format(res_name)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    sql = "SELECT IMAGE, RATING FROM RESTAURANT WHERE NAME = '{}'".format(res_name)
                    cursor.execute(sql)
                    result1 = cursor.fetchall()
                    for r in result1:
                        image = r[0]
                        rat = r[1]
                    if not image:
                        res_property['image'] = "static/homemodule/defaultres.jpg"
                    else:
                        res_property['image'] = image
                    if rat:
                        res_property['rat'] = rat
                    reviews = []
                    for r in result:
                        order_id = r[0]
                        rat = r[1]
                        des = r[2]
                        name = cursor.callfunc('PERSON_NAME',str,[order_id])
                        row = {'rat':rat,'des':des,'name':name}
                        reviews.append(row)
                    return render(request,'homemodule/restaurant.html',{'dict_result':dict_result,'reviews':reviews,'res_pro':res_property})
                else:
                    return render(request,'homemodule/restaurant.html',{'error':'Please Fill Up The SearchBox'})
    else:
        return redirect('loginuser')

def mycart(request):
    return render(request,'homemodule/cart.html')


def confirmOrder(request):
    if 'Person_id' in request.session:
        if (request.method == 'POST'):
            promo = request.POST.get('hpromo')
            print(promo)
            cursor = connection.cursor()
            sqlc = "SELECT COUNT(ORDER_ID) FROM ORDERS"
            cursor.execute(sqlc)
            result = cursor.fetchall()
            order_id = result[0][0] + 1
            print(order_id)
            request.session['order_id'] = str(order_id)
            sql = "INSERT INTO ORDERS(ORDER_ID,START_TIME,PERSON_ID,STATUS,PROMO_CODE) VALUES ('{}',SYSDATE,'{}','PENDING','{}')".format(order_id,request.session['Person_id'],promo)
            print(sql)
            cursor.execute(sql)
            foodids = request.POST.get('foodids')
            foodlist = foodids.split()
            print(foodlist)
            for i in range(int(len(foodlist)/2)):
                sqlo = "INSERT INTO ORDERED_ITEMS(ORDER_ID,FOOD_ID,AMOUNT) VALUES ("
                sqlo += str(order_id) + ","
                sqlo += foodlist[2*i] + "," + foodlist[2*i + 1] + ")"
                cursor.execute(sqlo)
            cursor.callproc('CALCULATE_PRICE',[order_id])
            return redirect('receiveOrder')
        else:
            if 'order_id' in request.session:
                return redirect('receiveOrder')
            else:
                print('No Order')
                cursor = connection.cursor()
                sql = "SELECT P.CODE, P.DISCOUNT_PCT, P.STATUS FROM PROMO P JOIN CUSTOMER_PROMO C ON (P.CODE = C.PROMO_CODE) WHERE P.STATUS = 'RUNNING' AND C.PERSON_ID = {}".format(request.session['Person_id'])
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                promo = []
                for r in result:
                    if r[2]=='RUNNING':
                        row = {'code':r[0],'discount':r[1],'status':r[2]}
                        promo.append(row)
                return render(request,'homemodule/confirmOrder.html',{'promo':promo})
    else:
        return redirect('loginuser')

def receiveOrder(request):
    if 'Person_id' in request.session:
        if request.method == 'GET':
            if 'order_id' in request.session:
                order_id = request.session['order_id']
                print("receice order")
                print(order_id)
                cursor = connection.cursor()
                total = cursor.callfunc('TOTAL_PRICE', int, [order_id])
                res_name = cursor.callfunc('res_name', str, [order_id])
                sql = "SELECT FIRST_NAME FROM PERSON WHERE PERSON_ID = (SELECT PERSON_ID FROM ORDERS WHERE ORDER_ID = {})".format(order_id)
                cursor.execute(sql)
                result = cursor.fetchall()
                name = result[0][0]
                sql = "SELECT NAME,PRICE,FOOD_ID FROM FOOD WHERE FOOD_ID IN ( SELECT FOOD_ID FROM ORDERED_ITEMS WHERE ORDER_ID = {})".format(order_id)
                cursor.execute(sql)
                result1 = cursor.fetchall()
                sql = "SELECT AMOUNT,FOOD_ID FROM ORDERED_ITEMS WHERE	ORDER_ID = {}".format(order_id)
                cursor.execute(sql)
                result2 = cursor.fetchall()
                dict_result = []
                for r1 in result1:
                    fn = r1[0]
                    price = r1[1]
                    amount = 0
                    for r2 in result2:
                        if r1[2] == r2[1]:
                            amount = r2[0]
                            break
                    row = {'food_name':fn,'price':price,'amount':amount}
                    dict_result.append(row)
                print(dict_result)
                orderInfo = {'orderON':'Order is ongoing. Please Wait...','order_id':order_id,'res_name':res_name,'total':total,'name':name}
                print(orderInfo)
                delivery = {}
                sql = "SELECT P.FIRST_NAME, P.PHONE FROM PERSON P JOIN DELIVERY_MAN D ON (P.PERSON_ID = D.PERSON_ID) WHERE DELIVERY_MAN_ID = (SELECT D.DELIVERY_MAN_ID FROM DELIVERY_MAN D JOIN ORDERS O ON (D.DELIVERY_MAN_ID = O.DELIVERY_MAN_ID) WHERE O.ORDER_ID = {})".format(order_id)
                cursor.execute(sql)
                result = cursor.fetchall()
                for r in result:
                    delivery = {'d_name':r[0],'d_phone':r[1]}
                print(delivery)
                return render(request, 'homemodule/receiveOrder.html',{'orderInfo':orderInfo,'order_items':dict_result,'delivery':delivery})
            else:
                return render(request, 'homemodule/receiveOrder.html',{'error':'No Order Is Placed Right Now'})
        else:
            comment = request.POST['comment']
            rat = request.POST.get('star')
            o_id = request.POST.get('order_id')
            print(comment + rat + str(o_id))
            cursor = connection.cursor()
            res_name = cursor.callfunc('res_name', str, [o_id])
            sql = "SELECT RESTAURANT_ID FROM RESTAURANT WHERE NAME = '{}'".format(res_name)
            cursor.execute(sql)
            result = cursor.fetchall()
            res_id = result[0][0]
            print("Res Id")
            print(res_id)
            sql = "SELECT COUNT(*) FROM REVIEWS"
            cursor.execute(sql)
            result = cursor.fetchall()
            r_id = result[0][0] + 1
            print("Review Id")
            print(r_id)
            sql = "INSERT INTO REVIEWS VALUES ('{}','{}','{}','{}','{}')".format(r_id,rat,comment,o_id,res_id)
            print(sql)
            try:
                cursor.execute(sql)
            except Exception as e:
                print("DatabaseError")
            return redirect('homelocation')
    else:
        return redirect('loginuser')


def extra(request):
    password = "12@weW322".encode()
    password = hashlib.sha256(password).hexdigest()
    print(password)
    return HttpResponse('<h1>Checked</h1>')

def myorders(request):
    cursor = connection.cursor()
    print(request.session['Person_id'])
    sql = "SELECT ORDER_ID, START_TIME, DELIVERY_TIME, COST, STATUS FROM ORDERS WHERE PERSON_ID = '{}' ORDER BY STATUS DESC".format(request.session['Person_id'])
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    dict_result = []
    for r in result:
        order_id = r[0]
        start_time = r[1]
        delivery_time = r[2]
        delivery_man_id = r[3]
        status = r[4]
        row = {'order_id':order_id,'start_time':start_time,
               'delivery_time':delivery_time, 'delivery_man_id':delivery_man_id,
                'status':status}
        dict_result.append(row)
    return render(request,'homemodule/myorders.html',{'orders':dict_result})
