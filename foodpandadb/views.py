from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .models import Job
from django.db import connection

# Create your views here.
def home(request):
    return render(request,'foodpanda/home.html')
def  list_person (request):
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
                'gender':gender, 'email':email, 'email':email, 'password':password,
                'phone':phone, 'birthdate':birthdate, 'regi_date':regi_date}
        dict_result.append(row)
    return render(request,'foodpanda/persons.html',{'persons' : dict_result})



def  customers (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM CUSTOMER"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        customer_id = r[0]
        person_id = r[1]
        location_id = r[2]
        row = {'customer_id':customer_id, 'person_id':person_id, 'location_id':location_id}
        dict_result.append(row)
    return render(request,'foodpanda/customers.html',{'customers' : dict_result})



def  delivery (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM DELIVERY_MAN"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        delivery_id = r[0]
        person_id = r[1]
        salary = r[2]
        image = r[3]
        row = {'delivery_id':delivery_id, 'person_id':person_id, 'salary':salary, 'image':image}
        dict_result.append(row)
    return render(request,'foodpanda/delivery.html',{'delivery' : dict_result})

def  locations (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM LOCATION"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        location_id = r[0]
        street_address = r[1]
        city = r[2]
        zip_code = r[3]
        row = {'location_id':location_id, 'street_address':street_address, 'city':city, 'zip_code':zip_code}
        dict_result.append(row)
    return render(request,'foodpanda/locations.html',{'locations' : dict_result})

def  food (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM FOOD"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        name = r[0]
        cuisine = r[1]
        price = r[2]
        availability = r[3]
        row = {'name':name, 'cuisine':cuisine, 'price':price, 'availability':availability}
        dict_result.append(row)
    return render(request,'foodpanda/foods.html',{'foods' : dict_result})

def  restaurant (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM RESTAURANT"
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
        row = {'restaurant_id':restaurant_id, 'name':name, 'location_id':location_id,
                'phone':phone, 'email':email, 'openning':openning,
                'closing':closing}
        dict_result.append(row)
    return render(request,'foodpanda/restaurants.html',{'restaurants' : dict_result})


def  orders (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM ORDERS"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        order_id = r[0]
        order_date = r[1]
        start_time = r[2]
        delivery_time = r[3]
        customer_id = r[4]
        delivery_id = r[5]
        status = r[6]
        row = {'order_id':order_id, 'order_date':order_date, 'start_time':start_time,
                'delivery_time':delivery_time, 'customer_id':customer_id, 'delivery_id':delivery_id,
                'status':status}
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
    cursor = connection.cursor()
    sql = "SELECT * FROM OFFERS"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        offer_id = r[0]
        food_id = r[1]
        discount_pct = r[2]
        max_discount = r[3]
        expire = r[4]
        restaurant_id = r[5]
        row = {'offer_id':offer_id, 'food_id':food_id, 'discount_pct':discount_pct, 'max_discount':max_discount,
        'expire':expire, 'restaurant_id':restaurant_id}
        dict_result.append(row)
    return render(request,'foodpanda/offers.html',{'offers' : dict_result})

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

def  menu (request):
    cursor = connection.cursor()
    sql = "SELECT * FROM MENU"
    cursor.execute(sql)
    result = cursor.fetchall()
    dict_result = []
    for r in result:
        resaurant_id = r[0]
        food_id = r[1]
        row = {'resaurant_id':resaurant_id, 'food_id':food_id}
        dict_result.append(row)
    return render(request,'foodpanda/menu.html',{'menu' : dict_result})
