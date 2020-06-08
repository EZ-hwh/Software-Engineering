from django.urls import path, re_path
from django.conf.urls import url, include
from . import views
import re

app_name = 'backend'
urlpatterns = [
    url('get_courseinfo', views.get_courseinfo),
    url('get_course_detail', views.get_course_detail),
    url('get_course_homework', views.get_course_homework),
    url('get_semester', views.get_semester),
    url('add_ddl', views.add_ddl),
    url('del_ddl',views.del_ddl),
    url('get_schedule', views.get_schedule),
    url('get_Todaylist', views.get_Todaylist),
    url('get_Weeklist', views.get_Weeklist),
    url('getcode', views.getcode),
    url('checkcode', views.checkcode),
    url('check_todolist', views.check_todolist),
    url('home', views.home),
    url('elearning_del_register', views.elearning_del_register),
    url('elearning_register', views.elearning_register),
    url('register', views.register_account),
    url('login', views.login_account, ),
    url('getcode', views.getcode),
    url('checkcode', views.checkcode),
    url('personal_create', views.personal_create),
    url('personal', views.personal),
    url('lesson', views.lesson),
    url('course', views.course),
    url('logout', views.logout_account),
    url('information', views.information),
    
    url('picture', views.picture),
    
    url('', views.first),
]
