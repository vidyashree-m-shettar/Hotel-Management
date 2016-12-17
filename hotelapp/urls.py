
from django.conf.urls import url
from django.contrib import admin
from views import welcome,listfood,listroom,liststarter,order,contact,sign_in,loginuser,about,user,sendSimpleEmail,logout_view


urlpatterns = [
    url(r'^$', welcome),
    url(r'food/',listfood),
    url(r'rooms/',listroom),
    url(r'starters/',liststarter),
    url(r'order/',order),
    url(r'contact',contact),
    url(r'signin',sign_in),
    url(r'login',loginuser),
    url(r'user',user),
    url(r'email1',sendSimpleEmail),
    url(r'about',about),
    url(r'logout',logout_view)

]
