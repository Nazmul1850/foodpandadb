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
            sql = "SELECT RESTAURANT_ID, NAME, PHONE_NO, OPENING, CLOSING FROM RESTAURANT WHERE RESTAURANT.LOCATION_ID = ( SELECT LOCATION_ID FROM LOCATION WHERE ((LONGITUDE - "
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
                row = {'id':id, 'name':name, 'phone':phone, 'openning':openning, 'closing':closing}
                dict_result.append(row)
            return render(request,'homemodule/home.html',{'address':adress,'restaurant':dict_result})
        else:
            res_name = request.POST['res_name']
            cursor = connection.cursor()
            sql = "SELECT FOOD_ID, NAME,CUISINE,PRICE,AVAILABILTY FROM FOOD WHERE RESTAURANT_ID = ( SELECT RESTAURANT_ID FROM RESTAURANT WHERE NAME = '"
            sql += str(res_name)
            sql += "')"
            cursor.execute(sql)
            result = cursor.fetchall()
            dict_result = {}
            request.session['foodID'] = ""
            for r in result:
                id = r[0]
                name = r[1]
                cuisine = r[2]
                price = r[3]
                avl = r[4]
                row = {'id':id, 'name':name,'cuisine':cuisine,'price':price,'avl':avl}
                try:
                    dict_result[cuisine].append(row)
                except Exception as e:
                    dict_result[cuisine] = []
                    dict_result[cuisine].append(row)
            print(dict_result)
            return render(request,'homemodule/restaurant.html',{'dict_result':dict_result})
    else:
        return redirect('loginuser')

def check(request):
    test = request.GET.get('text')
    print(test)
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
            sql = "INSERT INTO ORDERS(ORDER_ID,STAR_TIME,CUSTOMER_ID,STATUS) VALUES ("
            sql += str(order_id) + ","
            sql += "SYSDATE,"
            sql += request.session['Person_id'] + ","
            sql += "'PENDING')"
            #print(sql)
            cursor.execute(sql)
            foodids = request.POST['foodids']
            foodlist = foodids.split()
            for i in range(int(len(foodlist)/2)):
                sqlo = "INSERT INTO ORDERED_ITEMS(ORDER_ID,FOOD_ID,AMOUNT) VALUES ("
                sqlo += str(order_id) + ","
                sqlo += foodlist[2*i] + "," + foodlist[2*i + 1] + ")"
                cursor.execute(sqlo)
            return redirect('homelocation');
        else:
            return render(request,'homemodule/confirmOrder.html')
    else:
        return redirect('loginuser')
