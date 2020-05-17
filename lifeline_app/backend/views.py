from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from django.http.response import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .data import *

# Create your views here.

DEBUG = True  # 进行调试，用于输出调试
ACCOUNT_ID_RANGE = 100000000


@csrf_exempt
def first(request):
    if request.method == "GET":
        return render(request, 'index.html')


@csrf_exempt
def register_account(request):
    print("Register begin work")
    if request.method == "GET":
        return render(request, "register.html")
    if request.session.get('login', None):
        return HttpResponse("请退出登陆")
    if request.method == "POST":
        print(request)
        name = request.GET.get('name')
        pwd = request.GET.get("pass")
        # pwd_check = request.GET.get("pass_again")
        ret = {"flag": False, "error_msg": None}
        # if (pwd != pwd_check):
        #    ret['error_msg']="两次输入的密码不同"
        same_name_user = User.objects.filter(username=name)
        if same_name_user:
            ret["error_msg"] = "same user has been registered"
        else:
            ret["flag"] = True
            user = User.objects.create_user(username=name, password=pwd)
            request.session['login'] = True  # 注册后自动登陆
            request.session['email'] = user.email
            request.session['name'] = user.username
            account = Account.objects.create(user=user, nickname="None")
        return HttpResponse(json.dumps(ret), content_type="application/json")
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
    print(request.session.get('login', None))
    if request.session.get('login', None):  # 会话
        return redirect('/home')
        return HttpResponse("请勿重复登陆")  # 最好有个提示
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        print(request)
        name = request.GET.get('name')
        pwd = request.GET.get("pass")
        ret = {"flag": False, "error_msg": None}
        user = authenticate(username=name, password=pwd)
        if user:
            # 如果验证成功就让登录
            login(request, user)
            ret["flag"] = True
            request.session['login'] = True
            request.session['email'] = user.email
            request.session['name'] = user.username
            print("登陆成功")
        else:
            ret["error_msg"] = "用户名和密码错误"
            print("登陆错误")
        # else:
        #    ret["error_msg"] = "验证码错误"
        return HttpResponse(json.dumps(ret))


@csrf_exempt
def home(request):
    print("home begin work")
    if not request.session.get('login', None):
        return redirect('/login')
    if request.method == 'GET':  # 这里用于向前端传输数据用于渲染主页
        ret = {}
        user = Account.objects.get(user__username=request.session['name'])
        print(user.user.username, user.user.password)
        return render(request, 'home.html')


@csrf_exempt
def lesson(request):
    print("lesson begin work")
    if not request.session.get('login', None):
        return redirect('/login')
    if request.method == 'GET':
        return render(request, 'lessons.html')


@csrf_exempt
def personal(request):
    print("personal begin work")
    if not request.session.get('login', None):
        return redirect('/login')
    if request.method == 'GET':
        return render(request, 'personal.html')


@csrf_exempt
def course(request):
    print("course begin work")
    print(request)
    print(request.method)
    if not request.session.get('login', None):
        return redirect('/login')
    if request.method == 'GET':
        print("it work")
        # return render(request,'lessons.html')
        return render(request, 'SingleCourse.html')

@csrf_exempt
def get_schedule(request):
    if not request.session.get('login', None):
        return redirect('/login_page/')
    if request.method == 'GET':
        ret = {}

        user = Account.objects.get(email=request.session['email'])
        courses = [x.course for x in user.takeclass_set.all()]
        course_list = []
        for course in courses:
            info = {}
            info['name'] = course.course_name
            info['description'] = course.description
            info['time'] = [x.course_time for x in course.time_set.all()]
            course_list.append(info)

        schedulers = user.scheduler_set.all()
        scheduler_list = []
        for scheduler in scheduler_list:
            info = {}
            info['title'] = scheduler.title
            info['message'] = scheduler.message
            info['time'] = [x.course_time for x in scheduler.time_set.all()]
            scheduler_list.append(info)

        ret['course'] = course_list
        ret['schedule'] = scheduler_list
        return JsonResponse(ret)

@csrf_exempt
def get_Todaylist(request):
    if not request.session.get('login', None):
        return redirect('/login_page/')
    if request.method == 'GET':
        ret = []
        print("kaishi")
        test = True
        if test:
            global Status
            print("abc")
            ret = {
                "flag": True,
                "TodayList": [
                    {
                        "name": "Algorithm Assignment 3",
                        "time": "2020.5.9 10:30",
                        "description": "Complete 15-2.3,17.1",
                        "status": Status[1],
                        "id": 1
                    },
                    {
                        "name": "Software Engineer homework",
                        "time": "2020.5.9 18:30",
                        "description": "Implement the demo website.",
                        "status": Status[2],
                        "id": 2
                    },
                    {
                        "name": "Watch a movie",
                        "time": "2020.5.9 24:00",
                        "description": "",
                        "status": Status[3],
                        "id": 3
                    }
                ],
            }

            print(ret)
            return JsonResponse(ret)
        user = Account.objects.get(email = request.session['email'])
        todolist = user.todolist_set.all()
        todolist.order_by('deadline_time')

        for todo in todolist:
            now = {}
            now["name"] = todo.name
            now["time"] = todo.deadline_time
            now["description"] = todo.description
            ret.append(now)

        ret = {"TodayList": ret}
        return JsonResponse(ret)

Status = {1: 0, 2: 1, 3: 2, 4: 2, 5: 1, 6: 0}

@csrf_exempt
def get_Weeklist(request):
    if not request.session.get('login', None):
        return redirect('/login_page/')
    if request.method == 'GET':
        ret = []
        print("kaishiWeek")
        test = True
        if test:
            global Status
            ret = {
                "flag": True,
                "WeekList": [
                    {
                        "name": "Algorithm Assignment 3",
                        "time": "2020.5.9 10:30",
                        "description": "Complete 15-2.3,17.1",
                        "status": Status[4],
                        "id": 4
                    },
                    {
                        "name": "Software Engineer homework",
                        "time": "2020.5.9 18:30",
                        "description": "Implement the demo website.",
                        "status": Status[5],
                        "id": 5
                    },
                    {
                        "name": "Watch a movie",
                        "time": "2020.5.9 24:00",
                        "description": "",
                        "status": Status[6],
                        "id": 6
                    }
                ],
            }
            return JsonResponse(ret)
        user = Account.objects.get(email=request.session['email'])
        Weeklist = user.todolist_set.all()
        Weeklist.order_by('deadline_time')

        for todo in Weeklist:
            now = {}
            now["name"] = todo.name
            now["time"] = todo.deadline_time
            now["description"] = todo.description
            ret.append(now)

        ret = {"WeekList": ret}
        return JsonResponse(ret)


@csrf_exempt
def checkcode(request):
    if request.method == 'POST':
        ret = {}
        try:
            register = Register.objects.get(email = request.GET.get("email"))
            if request.GET.get("code") == register.checksum:
                ret["flag"] = True
            else:
                ret["flag"] = False
                ret["error_msg"] = "验证码错误！"
        except:
            ret["flag"] = False
            ret["error_msg"] = "请您请求验证码！"
        return JsonResponse(ret)

@csrf_exempt
def getcode(request):
    if request.method == 'POST':
        print("getcode begin!!!")
        email = request.GET.get("email")
        ret = {}
        if Account.objects.filter(email = email).exists():
            ret["flag"] = False
            ret["error_msg"] = "邮箱已注册！"
            return JsonResponse(ret)
        try:
            register = Register.objects.get(email = email)
            print("try")
        except:
            register = Register(email = email)
            print("except")
        register.checksum = random.randint(1000, 9999)
        print(register.email, register.checksum)
        register.save()
        # ret["checksum"] = register.checksum
        ret["flag"] = True
        return JsonResponse(ret)


@csrf_exempt
def logout(request):  # 登出,此方案过于简单，需改进
    request.session['login'] = False
    return render(request,'index.html')

@csrf_exempt
def check_todolist(request):
    if not request.session.get('login', None):
        return redirect('/login_page/')
    if request.method == 'GET':
        ret = {}
        test = True
        if test:
            global Status
            switch = {0: 0, 1: 1, 2: 2}
            status = request.GET["status"]
            if status not in switch:
                ret["flag"] = False
                ret["error_msg"] = "Wrong status!"
                return JsonResponse(ret)
            Status[request.GET.get("id")] = status
            ret["flag"] = True
            return JsonResponse(ret)



        if not Todolist.objects.filter(todolist_id = request.GET.get("id")).exists():
            ret["flag"] = False
            ret["error_msg"] = "Todolist id doen'st exist!"
            return JsonResponse(ret)
        Todo = Todolist.objects.get(todolist_id = request.GET.get("id"))
        if Todo.account.email != request.session["email"]:
            ret["flag"] = False
            ret["error_msg"] = "Your account doesn't own this todolist!"
            return JsonResponse(ret)
        switch = {0: 0, 1: 1, 2: 2}
        status = request.GET["status"]
        if status not in switch:
            ret["flag"] = False
            ret["error_msg"] = "Wrong status!"
            return JsonResponse(ret)
        Todo.status = status
        ret["flag"] = True
        return JsonResponse(ret)

@csrf_exempt
def get_semester(request):
    if not request.session.get('login', None):
        return redirect('/login_page/')
    test = True
    if test:
        ret = get_course_sample_data()
        return JsonResponse(ret)