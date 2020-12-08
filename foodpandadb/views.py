from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
#from .models import Job
from django.db import connection

# Create your views here.
def foodpandadmin(request):
    if 'Admin_id' in request.session:
        return render(request,'foodpanda/home.html')
    else:
        return redirect('loginadmin')
def loginadmin(request):
    if (request.method == 'GET'):
        return render(request,'foodpanda/loginadmin.html',{'form':AuthenticationForm()})
    else:
        cursor = connection.cursor()
        username = request.POST['username']
        password = request.POST['password']
        sql = "SELECT ADMIN_ID, ADMIN_NAME FROM ADMIN WHERE ADMIN_NAME = "
        sql += "'"
        sql += username
        sql += "'"
        sql += "AND ADMIN_PASSWORD = "
        sql += "'"
        sql += password
        sql += "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if not bool(result):
            return render(request, 'foodpanda/loginadmin.html',{'form':AuthenticationForm(), 'error':'Email or Password is Wrong'})
        else:
            for r in result:
                admin_id = r[0]
                name = r[1]
            request.session['Admin_id'] = str(admin_id)
            request.session['Admin_name'] = name
            return redirect('foodpandadmin')
def logoutadmin(request):
    try:
        del request.session['Admin_id']
        del request.session['Admin_name']
    except KeyError:
        pass
    return redirect('loginadmin')


def  list_person (request):
    if 'Admin_id' in request.session:
        cursor = connection.cursor()
        sql = "SELECT * FROM PERSON"
        cursor.execute(sql)
        result = cursor.fetchall()
        dict_result = []
        for r in result:
            person_id = r[0]
            first_name = r[1]
            last_name = r[2]
            gender = r[3]
            email = r[4]
            password = r[5]
            phone = r[6]
            birthdate = r[7]
            regi_date = r[8]
            row = {'person_id':person_id, 'first_name':first_name, 'last_name':last_name,
                    'gender':gender, 'email':email, 'password':password,
                    'phone':phone, 'birthdate':birthdate, 'regi_date':regi_date}
            dict_result.append(row)
        return render(request,'foodpanda/persons.html',{'persons' : dict_result})
    else:
        return redirect('loginadmin')



def  food (request):
    res_id = request.session['res_id']
    cursor = connection.cursor()
    sql = "SELECT NAME FROM RESTAURANT WHERE RESTAURANT_ID = '{}'".format(res_id)
    cursor.execute(sql)
    name = cursor.fetchall()
    food_res_id = {'res_id':res_id,'name':name[0][0]}
    sql = "SELECT * FROM FOOD WHERE RESTAURANT_ID = '{}'".format(res_id)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    dict_result = []
    for r in result:
        id = r[0]
        name = r[1]
        cuisine = r[2]
        price = r[3]
        availability = r[4]
        offer_price = r[6]
        row = {'id':id, 'name':name, 'cuisine':cuisine, 'price':price, 'availability':availability,'offer_price':offer_price}
        dict_result.append(row)
    return render(request,'foodpanda/foods.html',{'foods' : dict_result,'food_res_id':food_res_id})


def  restaurant (request):
    if 'Admin_id' in request.session:
        if request.method == 'GET':
            cursor = connection.cursor()
            sql = "SELECT * FROM RESTAURANT ORDER BY RESTAURANT_ID"
            cursor.execute(sql)
            result = cursor.fetchall()
            dict_result = []
            for r in result:
                restaurant_id = r[0]
                name = r[1]
                location_id = r[2]
                phone = r[3]
                email = r[4]
                openning = r[5]
                closing = r[6]
                image = r[7]
                row = {'restaurant_id':restaurant_id, 'name':name, 'location_id':location_id,
                        'phone':phone, 'email':email, 'openning':openning,
                        'closing':closing,'image':image}
                dict_result.append(row)
            return render(request,'foodpanda/restaurants.html',{'restaurants' : dict_result})
        else:
            return redirect('loginadmin')
    else:
        return redirect('loginadmin')

def  locations (request):
    if 'Admin_id' in request.session:
        cursor = connection.cursor()
        sql = "SELECT * FROM LOCATION"
        cursor.execute(sql)
        result = cursor.fetchall()
        dict_result = []
        for r in result:
            longitude = r[1]
            latitude = r[2]
            city = r[3]
            zip_code = r[4]
            row = {'longitude':longitude,'latitude':latitude, 'city':city, 'zip_code':zip_code}
            dict_result.append(row)
        return render(request,'foodpanda/locations.html',{'locations' : dict_result})
    else:
        return redirect('loginadmin')


def  orders (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM ORDERS"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        order_id = r[0]
        start_time = r[1]
        delivery_time = r[2]
        delivery_man_id = r[3]
        status = r[4]
        person_id = r[5]
        row = {'order_id':order_id, 'start_time':start_time,
                'delivery_time':delivery_time,'delivery_man_id':delivery_man_id,
                'status':status,'person_id':person_id}
        dict_result.append(row)
    return render(request,'foodpanda/orders.html',{'orders' : dict_result})


def  promos (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM PROMO"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        code = r[0]
        discount_pct = r[1]
        start = r[2]
        end = r[3]
        status = r[4]
        row = {'code':code, 'discount_pct':discount_pct, 'start':start, 'end':end, 'status':status}
        dict_result.append(row)
    return render(request,'foodpanda/promos.html',{'promos' : dict_result})

def  payments (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM PAYMENTS"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        payment_id = r[0]
        amount = r[1]
        method = r[2]
        promo_code = r[3]
        order_id = r[4]
        row = {'payment_id':payment_id, 'amount':amount, 'method':method, 'promo_code':promo_code, 'order_id':order_id}
        dict_result.append(row)
    return render(request,'foodpanda/payments.html',{'payments' : dict_result})

def  offers (request):
    res_id = request.session['res_id']
    cursor = connection.cursor()
    sql = "SELECT NAME FROM RESTAURANT WHERE RESTAURANT_ID = '{}'".format(res_id)
    cursor.execute(sql)
    name = cursor.fetchall()
    offer_res_id = {'res_id':res_id,'name':name[0][0]}
    sql = "SELECT * FROM OFFERS WHERE RESTAURANT_ID = '{}'".format(res_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        offer_id = r[0]
        discount_pct = r[1]
        max_discount = r[2]
        expire = r[3]
        start_date = r[5]
        row = {'offer_id':offer_id,'discount_pct':discount_pct, 'max_discount':max_discount,
        'expire':expire,'start_date':start_date}
        dict_result.append(row)
    return render(request,'foodpanda/offers.html',{'offers' : dict_result,'offer_res_id':offer_res_id})

def  reviews (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM REVIEWS"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        review_id = r[0]
        rating = r[1]
        description = r[2]
        food_id = r[3]
        customer_id = r[4]
        order_id = r[5]
        row = {'review_id':review_id, 'rating':rating, 'description':description, 'food_id':food_id,
        'customer_id':customer_id, 'order_id':order_id}
        dict_result.append(row)
    return render(request,'foodpanda/reviews.html',{'reviews' : dict_result})

def  customer_promo (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM CUSTOMER_PROMO"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        customer_id = r[0]
        promo_code = r[1]
        row = {'customer_id':customer_id, 'promo_code':promo_code}
        dict_result.append(row)
    return render(request,'foodpanda/customer_promo.html',{'customer_promo' : dict_result})

def  orderd_items (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM ORDERED_ITEMS"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        order_id = r[0]
        food_id = r[1]
        row = {'order_id':order_id, 'food_id':food_id}
        dict_result.append(row)
    return render(request,'foodpanda/orderd_items.html',{'orderd_items' : dict_result})
