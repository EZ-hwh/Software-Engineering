from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

DEBUG = True #进行调试，用于输出调试
ACCOUNT_ID_RANGE = 100000000

@csrf_exempt
def first(request):
    if request.method == "GET":
        return render(request, 'index.html')
    print("ok")
    back_dir = {"msg":"ok"}
    return HttpResponse(json.dumps(back_dir))
    if request.method == "POST":
        mode = request.GET.get('mode')
        if mode == 'login':
            HttpResponse("ok")
            render(request,'login.html')
        elif mode == 'register':
            HttpResponse("ok")
            render(request,'register.html')
        HttpResponse("ok")
    print("ok")
    HttpResponse("ok")

@csrf_exempt
def register_account(request):
    print("Register begin work")
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        print(request)
        name = request.GET.get('name')
        pwd = request.GET.get("pass")
        #pwd_check = request.GET.get("pass_again")
        ret = {"flag":False,"error_msg":None}
        #if (pwd != pwd_check):
        #    ret['error_msg']="两次输入的密码不同"
        same_name_user = User.objects.filter(username=name)
        if same_name_user:
            ret["error_msg"] = "same user has been registered"
        else:
            ret["flag"] = True
            user = User.objects.create_user(username=name,password=pwd)
            account = Account.objects.create(user=user,nickname="None")
        print(ret)
        return HttpResponse(json.dumps(ret),content_type="application/json")
    '''
        try:
            account = Account.objects.filter(username=name)
        except Account.DoesNotExist:
            if pwd == pwd_check:
                while True:
                    random_id = random.randint(1,ACCOUNT_ID_RANGE)
                    try:
                        account_id = Account.objects.filter(account_id=random_id)
                    except Account.DoesNotExist:
                        break
                Account.objects.create(account_id=random_id,username=name,password=pwd,nickname=name)
            else:

                HttpResponse(json.dumps)
                
        if DEBUG:
            print(account)
        return HttpResponse(json.dumps(ret))
    #content = request.GET['reg']
    '''

@csrf_exempt
def login_account(request):
    print("Login begin work")
    if request.method == "GET":
        print("asdf")
        return render(request,"login.html")
    if request.method == "POST":
        print(request)
        name = request.GET.get('name')
        pwd = request.GET.get("pass")
        ret = {"flag":False,"error_msg":None}
        user = authenticate(username=name, password=pwd)
        if user:
            #如果验证成功就让登录
            login(request,user)
            ret["flag"] = True
            print("登陆成功")
        else:
            ret["error_msg"] = "用户名和密码错误"
            print("登陆错误")
        #else:
        #    ret["error_msg"] = "验证码错误"
        return HttpResponse(json.dumps(ret))