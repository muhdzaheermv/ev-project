from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def ev_login(request):
    return render(request,'ev_login.html')

def ev_signup(request):
    return render(request,'ev_signup.html')

def ev_station_login(request):
    return render(request,'ev_station_login.html')

def ev_station_signup(request):
    return render(request,'ev_station_signup.html')


