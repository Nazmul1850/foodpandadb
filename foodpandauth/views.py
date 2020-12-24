from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import connection
from django.db import IntegrityError
import hashlib;
# Create your views here.

def home(request):
    if 'Person_id' in request.session:
        return redirect('homelocation')
    else:
        return redirect('loginuser')

def signupuser(request):
    adress = {'latitude':request.ipinfo.latitude,
              'longitude':request.ipinfo.longitude,
              'postal':request.ipinfo.postal,
              'city':request.ipinfo.city}
    if (request.method == 'GET'):
        return render(request, 'foodpandauth/signup.html',{'form':UserCreationForm()})
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
            sql = "INSERT INTO PERSON(PERSON_ID, EMAIL, PASSWORD, REGISTRATION_DATE) VALUES ('"
            sql += str(count_id)
            sql += "','"
            sql += email
            sql += "','"
            sql += password
            sql += "', SYSDATE)"
            try:
                cursor.execute(sql)
                request.session['Person_id'] = str(count_id)
                return redirect('updateProfile')
            except IntegrityError as e:
                return render(request, 'foodpandauth/signup.html',{'form':UserCreationForm(),'error':"Email Taken Or Password is weak"})
        else:
            return render(request, 'foodpandauth/signup.html',{'form':UserCreationForm(),'error':"Email Taken Or Password is weak"})

def loginuser(request):
    if (request.method == 'GET'):
        return render(request,'foodpandauth/login.html',{'form':AuthenticationForm()})
    else:
        cursor = connection.cursor()
        email = request.POST['username']
        password = request.POST['password']
        password = password.encode()
        password = hashlib.sha256(password).hexdigest()
        sql = "SELECT PERSON_ID, FIRST_NAME FROM PERSON WHERE EMAIL = "
        sql += "'"
        sql += email
        sql += "'"
        sql += "AND PASSWORD ="
        sql += "'"
        sql += password
        sql += "'"
        cursor.execute(sql)
        result = cursor.fetchall()
        if not bool(result):
            return render(request, 'foodpandauth/login.html',{'form':AuthenticationForm(), 'error':'Email or Password is Wrong'})
        else:
            for r in result:
                person_id = r[0]
                name = r[1]
            request.session['Person_id'] = str(person_id)
            request.session['name'] = name
            return redirect('homelocation')


def logoutuser(request):
    try:
        del request.session['Person_id']
        del request.session['name']
    except KeyError:
        pass
    return redirect('loginuser')

def updateProfile(request):
    if 'Person_id' in request.session:
        if (request.method == 'GET'):
            cursor = connection.cursor()
            sql = "SELECT FIRST_NAME, LAST_NAME, GENDER, PHONE, TO_CHAR(BIRTH_DATE, 'yyyy-mm-dd') FROM PERSON WHERE PERSON_ID = "
            sql += request.session['Person_id']
            cursor.execute(sql)
            result = cursor.fetchall()
            dict_result = {'first_name':result[0][0],'last_name':result[0][1],'gender':result[0][2],
                            'phone':result[0][3],'birthdate':result[0][4]}
            return render(request,'foodpandauth/updateprofile.html',{'dict_result':dict_result})
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            phone = request.POST['phone']
            birthdate = request.POST['birthdate']
            cursor = connection.cursor()
            sql = "UPDATE PERSON SET FIRST_NAME = '"
            sql += first_name
            sql += "', LAST_NAME = '"
            sql += last_name
            sql += "', GENDER = '"
            sql += gender
            sql += "', PHONE = '"
            sql += str(phone)
            sql += "', BIRTH_DATE = TO_DATE('"
            sql += str(birthdate)
            sql += "', 'YYYY-MM-DD')"
            sql += " WHERE PERSON_ID = "
            sql += request.session['Person_id']
            request.session['name'] = first_name
            cursor.execute(sql)
            return redirect('homelocation')
    else:
        return render(request,'foodpandauth/updateprofile.html',{'error':'log in first'})
