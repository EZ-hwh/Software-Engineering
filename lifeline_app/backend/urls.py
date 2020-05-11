from django.urls import path, re_path
from django.conf.urls import url, include
from . import views
import re

app_name = 'backend'
urlpatterns = [
    url('get_schedule', views.get_schedule),
    url('get_Todaylist', views.get_Todaylist),
    url('get_Weeklist', views.get_Weeklist),
    url('getcode', views.getcode),
    url('checkcode', views.checkcode),
    url('home', views.home),
    url('register', views.register_account, ),
    url('login', views.login_account, ),
    url('getcode', views.getcode),
    url('checkcode', views.checkcode),
    url('personal', views.personal),
    url('lesson', views.lesson),
    url('course', views.course),
    url('logout', views.logout),
    url('', views.first, ),
]
