from django.urls import path,re_path
from django.conf.urls import url,include
from . import views
import re

app_name='backend'
urlpatterns = [
    url('get_schedule', views.get_schedule),
    usl('get_todolist', views.get_todolist)
    url('home',views.home),
    url('register',views.register_account,),
    url('login',views.login_account,),
    url('lesson',views.lesson),
    url('course',views.course),
    url('logout',views.logout),
    url('',views.first,),
]