from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'homemodule/home.html')

def location(request):
    response_string = 'The IP address {} is located at the coordinates {}, which is in the city {}.'.format(
        request.ipinfo.ip,
        request.ipinfo.loc,
        request.ipinfo.city
    )
    return render(request,'homemodule/home.html')
