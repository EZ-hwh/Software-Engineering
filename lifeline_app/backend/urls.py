from django.urls import path,re_path
from django.conf.urls import url,include
from . import views
import re

app_name='backend'
urlpatterns = [
    url('register',views.register_account,),
    url('login',views.login_account,),
]