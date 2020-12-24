from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
#from .models import Job
from django.db import connection
from django.db import IntegrityError
import hashlib

# Create your views here.
def delivery(request):
    if 'Delivery_id' in request.session:
        if request.method == 'GET':
            cursor = connection.cursor()
            sql = "SELECT O.ORDER_ID, O.START_TIME, P.FIRST_NAME FROM PERSON P JOIN ORDERS O ON(P.PERSON_ID = O.PERSON_ID) WHERE O.STATUS = 'PENDING'"
            cursor.execute(sql)
            result = cursor.fetchall()
            dict_result = []
            for r in result:
                row = {'order_id':r[0],'start':r[1],'person':r[2]}
                dict_result.append(row)
            return render(request,'delivery/home.html',{'orders':dict_result})
        else:
            order_id = request.POST['order_id']
            cursor = connection.cursor()
            total = cursor.callfunc('TOTAL_PRICE', int, [order_id])
            res_name = cursor.callfunc('res_name', str, [order_id])
            dict_result = {'order_id':order_id,'total':total,'res_name':res_name}
            return render(request,'delivery/singleOrder.html',{'info':dict_result})
    else:
        return redirect('logindelivery')

def logindelivery(request):
    if (request.method == 'GET'):
        return render(request,'delivery/login.html',{'form':AuthenticationForm()})
    else:
        cursor = connection.cursor()
        email = request.POST['username']
        password = request.POST['password']
        password = password.encode()
        password = hashlib.sha256(password).hexdigest()
        sql = "SELECT P.PERSON_ID, P.FIRST_NAME, D.DELIVERY_MAN_ID FROM PERSON P JOIN DELIVERY_MAN D ON (P.PERSON_ID = D.PERSON_ID) WHERE P.EMAIL = '{}' AND P.PASSWORD = '{}'".format(email,password)
        cursor.execute(sql)
        result = cursor.fetchall()
        if not bool(result):
            return render(request, 'delivery/login.html',{'form':AuthenticationForm(), 'error':'Email or Password is Wrong'})
        else:
            for r in result:
                person_id = r[2]
                name = r[1]
            request.session['Delivery_id'] = str(person_id)
            request.session['Delivery_name'] = name
            return redirect('delivery')
def logoutdelivery(request):
    try:
        del request.session['Delivery_id']
        del request.session['Delivery_name']
    except KeyError:
        pass
    return redirect('logindelivery')

def signupDelivery(request):
    adress = {'latitude':request.ipinfo.latitude,
              'longitude':request.ipinfo.longitude,
              'postal':request.ipinfo.postal,
              'city':request.ipinfo.city}
    if (request.method == 'GET'):
        return render(request, 'delivery/signup.html')
    else :
        if request.POST['password1'] == request.POST['password2']:
            cursor = connection.cursor()
            email = request.POST['username']
            password = request.POST['password1']
            password = password.encode()
            password = hashlib.sha256(password).hexdigest()
            countsql = "SELECT COUNT(*) FROM PERSON"
            cursor.execute(countsql)
            result = cursor.fetchall()
            count_id = result[0][0] + 1
            sql = "INSERT INTO PERSON (PERSON_ID, EMAIL, PASSWORD, REGISTRATION_DATE) VALUES ('{}','{}','{}',SYSDATE)".format(count_id,email,password)
            print(sql)
            try:
                cursor.execute(sql)
                sql = "SELECT COUNT(*) FROM DELIVERY_MAN"
                cursor.execute(sql)
                result = cursor.fetchall()
                d_id = result[0][0] + 1;
                sql = "INSERT INTO DELIVERY_MAN VALUES ('{}','{}','200')".format(d_id,count_id)
                cursor.execute(sql)
                request.session['Delivery_id'] = str(d_id)
                return redirect('updateDelivery')
            except IntegrityError as e:
                return render(request, 'delivery/signup.html',{'error':"Email Taken Or Password is weak"})
        else:
            return render(request, 'delivery/signup.html',{'error':"Email Taken Or Password is weak"})

def updateDelivery(request):
    if 'Delivery_id' in request.session:
        if (request.method == 'GET'):
            cursor = connection.cursor()
            sql = "SELECT P.FIRST_NAME, P.LAST_NAME, P.GENDER, P.PHONE, TO_CHAR(P.BIRTH_DATE, 'yyyy-mm-dd') FROM PERSON P JOIN DELIVERY_MAN D ON (P.PERSON_ID = D.PERSON_ID) WHERE D.DELIVERY_MAN_ID = {}".format(request.session['Delivery_id'])
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            dict_result = {}
            for r in result:
                dict_result = {'first_name':r[0],'last_name':r[1],'gender':r[2],'phone':r[3],'birthdate':r[4]}
            return render(request,'delivery/updateDelivery.html',{'dict_result':dict_result})
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            phone = request.POST['phone']
            birthdate = request.POST['birthdate']
            cursor = connection.cursor()
            del_id = request.session['Delivery_id']
            sql = "UPDATE PERSON SET FIRST_NAME = '{}',LAST_NAME = '{}',GENDER = '{}',PHONE = '{}', BIRTH_DATE = TO_DATE('{}','YYYY-MM-DD') WHERE PERSON_ID = (SELECT PERSON_ID FROM DELIVERY_MAN WHERE DELIVERY_MAN_ID = {})".format(first_name,last_name,gender,phone,birthdate,del_id)
            request.session['Delivery_name'] = first_name
            cursor.execute(sql)
            return redirect('delivery')
    else:
        return render(request,'delivery/updateDelivry.html',{'error':'log in first'})
