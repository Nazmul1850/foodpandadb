from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .models import Job
from django.db import connection

# Create your views here.
def home(request):
    return render(request,'foodpanda/home.html')
def  list_person (request):
    # cursor = connection.cursor()
    # sql = "INSERT INTO JOBS VALUES(%s,%s,%s,%s)"
    # cursor.execute(sql,['NEW_JOB_1','Something New 1',5000,9000])
    # connection.commit()
    # cursor.close()

    cursor = connection.cursor()
    sql = "SELECT * FROM PERSONS"
    cursor.execute(sql)
    result = cursor.fetchall()

    # cursor = connection.cursor()
    # sql = "SELECT * FROM JOBS WHERE MIN_SALARY=%s"
    # cursor.execute(sql,[5000])
    # result = cursor.fetchall()
    # cursor.close()

    dict_result = []
    for r in result:
        person_id = r[0]
        first_name = r[1]
        last_name = r[2]
        street_address = r[3]
        city = r[4]
        zip_code = r[5]
        gender = r[6]
        email = r[7]
        password = r[8]
        phone = r[9]
        birthdate = r[10]
        regi_date = r[11]
        row = {'person_id':person_id, 'first_name':first_name, 'last_name':last_name,
                'street_address':street_address, 'city':city, 'zip_code':zip_code,
                'gender':gender, 'email':email, 'email':email, 'password':password,
                'phone':phone, 'birthdate':birthdate, 'regi_date':regi_date }
        dict_result.append(row)

    #return render(request,'list_jobs.html',{'jobs' : Job.objects.all()})
    return render(request,'foodpanda/dbconnect.html',{'persons' : dict_result})
