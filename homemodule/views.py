from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from array import array
import js2py

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
            sql = "SELECT RESTAURANT_ID, NAME, PHONE_NO, OPENING, CLOSING, IMAGE FROM RESTAURANT WHERE RESTAURANT.LOCATION_ID IN ( SELECT LOCATION_ID FROM LOCATION WHERE ((LONGITUDE - "
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
                row = {'id':id, 'name':name, 'phone':phone, 'openning':openning, 'closing':closing, 'image':image}
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
                sql = "SELECT RESTAURANT_ID, NAME, PHONE_NO, OPENING, CLOSING, IMAGE FROM RESTAURANT WHERE RESTAURANT_ID IN {}".format(result)
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
                    row = {'id':id, 'name':name, 'phone':phone, 'openning':openning, 'closing':closing, 'image':image}
                    dict_result.append(row)
                return render(request,'homemodule/home.html',{'address':adress,'restaurant':dict_result})
            else:
                if res_name:
                    cursor = connection.cursor()
                    sql = "SELECT FOOD_ID, NAME,CUISINE,PRICE,AVAILABILTY, OFFER_PRICE FROM FOOD WHERE RESTAURANT_ID = ( SELECT RESTAURANT_ID FROM RESTAURANT WHERE NAME = '"
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
                        if avl == 'y' or avl == 'Y':
                            if price == offer_price:
                                row = {'res_name':res_name, 'id':id, 'name':name,'cuisine':cuisine,'price':price,'avl':avl,'offer_price':offer_price,'status':0}
                            else:
                                row = {'res_name':res_name, 'id':id, 'name':name,'cuisine':cuisine,'price':price,'avl':avl,'offer_price':offer_price,'status':1}
                        else:
                            continue;
                        try:
                            dict_result[cuisine].append(row)
                        except Exception as e:
                            dict_result[cuisine] = []
                            dict_result[cuisine].append(row)
                    #print(dict_result)
                    return render(request,'homemodule/restaurant.html',{'dict_result':dict_result})
                else:
                    return render(request,'homemodule/restaurant.html',{'error':'Please Fill Up The SearchBox'})
    else:
        return redirect('loginuser')

def check(request):
    if 'order_id' in request.session:
        del request.session['order_id']
    return redirect('loginuser')


def confirmOrder(request):
    if 'Person_id' in request.session:
        if (request.method == 'POST'):
            cursor = connection.cursor()
            sqlc = "SELECT COUNT(ORDER_ID) FROM ORDERS"
            cursor.execute(sqlc)
            result = cursor.fetchall()
            order_id = result[0][0] + 1
            print(order_id)
            request.session['order_id'] = str(order_id)
            sql = "INSERT INTO ORDERS(ORDER_ID,START_TIME,PERSON_ID,STATUS,DELIVERY_MAN_ID) VALUES ("
            sql += str(order_id) + ","
            sql += "SYSDATE,"
            sql += request.session['Person_id'] + ","
            sql += "'PENDING', 1)"
            #print(sql)
            cursor.execute(sql)
            foodids = request.POST['foodids']
            foodlist = foodids.split()
            print(foodlist)
            for i in range(int(len(foodlist)/2)):
                sqlo = "INSERT INTO ORDERED_ITEMS(ORDER_ID,FOOD_ID,AMOUNT) VALUES ("
                sqlo += str(order_id) + ","
                sqlo += foodlist[2*i] + "," + foodlist[2*i + 1] + ")"
                cursor.execute(sqlo)
            return redirect('receiveOrder')
        else:
            if 'order_id' in request.session:
                return redirect('receiveOrder')
            else:
                print('No Order')
                return render(request,'homemodule/confirmOrder.html')
    else:
        return redirect('loginuser')

def receiveOrder(request):
    if 'Person_id' in request.session:
        if request.method == 'GET':
            order_id = request.session['order_id']
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
            return render(request, 'homemodule/receiveOrder.html',{'orderInfo':orderInfo,'order_items':dict_result})
        else:
            comment = request.POST['comment']
            rat = request.POST.get('star')
            o_id = request.POST.get('order_id')
            #print(coment + rat + o_id)
            cursor = connection.cursor()
            sql = "SELECT COUNT(*) FROM REVIEWS"
            cursor.execute(sql)
            result = cursor.fetchall()
            r_id = result[0][0] + 1
            sql = "INSERT INTO REVIEWS VALUES ('{}','{}','{}','{}')".format(r_id,rat,comment,o_id)
            print(sql)
            try:
                cursor.execute(sql)
            except Exception as e:
                print("DatabaseError")
            return redirect('homelocation')
    else:
        return redirect('loginuser')


def myorders(request):
    cursor = connection.cursor()
    sql = "SELECT ORDER_ID, START_TIME, DELIVERY_TIME, DELIVERY_MAN_ID, STATUS FROM ORDERS WHERE PERSON_ID = " + request.session['Person_id']
    sql += "ORDER BY STATUS DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
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
