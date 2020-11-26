from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
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
        sql = "SELECT NAME,CUISINE,PRICE,AVAILABILTY FROM FOOD WHERE RESTAURANT_ID = ( SELECT RESTAURANT_ID FROM RESTAURANT WHERE NAME = '"
        sql += str(res_name)
        sql += "')"
        cursor.execute(sql)
        result = cursor.fetchall()
        dict_result = {}
        for r in result:
            name = r[0]
            cuisine = r[1]
            price = r[2]
            avl = r[3]
            row = {'name':name,'cuisine':cuisine,'price':price,'avl':avl}
            try:
                dict_result[cuisine].append(row)
            except Exception as e:
                dict_result[cuisine] = []
                dict_result[cuisine].append(row)
        print(dict_result)
        return render(request,'homemodule/restaurant.html',{'dict_result':dict_result})


#
# def showRestaurant(request):
#     return render(request,'homemodule/restaurant.html')
