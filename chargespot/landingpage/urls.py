from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ev_login',views.ev_login,name='ev_login'),
    path('ev_signup',views.ev_signup,name='ev_signup'),
    path('ev_station_login',views.ev_station_login,name='ev_station_login'),
    path('ev_station_signup',views.ev_station_signup,name='ev_station_signup'),
]
