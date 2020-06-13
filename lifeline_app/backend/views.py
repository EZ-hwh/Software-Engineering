from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.http.response import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
import random
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .data import *
from .crwaller import *

# Create your views here.

DEBUG = True  # 进行调试，用于输出调试
ACCOUNT_ID_RANGE = 100000000


def login_uis(request):  # 帮绑定了elearning的用户登陆uis
    account = Account.objects.get(user=request.user)
    print("Trying to login uis.")
    # print(account.elearning_login)
    if account.elearning_login:
        if not request.session["elearning_login"]:
            print("Backend: elearning login.")
            request.session["elearning_session"], request.session["elearning_login"] = login_elearning(
                account.elearning_name, account.elearning_password)
        if not request.session["jwfw_login"]:
            print("Backend: jwfw login.")
            request.session["jwfw_session"], request.session["jwfw_login"] = login_jwfw(account.elearning_name,
                                                                                        account.elearning_password)
        return True
    else:
        return False


@csrf_exempt
def first(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == "GET":
        return render(request, 'index.html')


@csrf_exempt
def register_account(request):
    print("Register begin work")
    if request.user.is_authenticated:
        return HttpResponse("Already logged in.")
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        name = request.GET.get('name')
        pwd = request.GET.get("pass")
        email = request.GET.get('email')
        ret = {"flag": False, "error_msg": None}
        same_name_user = User.objects.filter(username=name)
        if same_name_user:
            ret["error_msg"] = "same user has been registered"
        else:
            ret["flag"] = True
            user = User.objects.create_user(username=name, password=pwd, email=email)
            login(request, user)
            request.session["elearning_login"] = False
            request.session["jwfw_login"] = False
            account = Account.objects.create(user=user, nickname=name, email=email)
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
    if request.user.is_authenticated:  # 会话
        return redirect('/home')
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        print(request)
        name = request.GET.get('name')
        pwd = request.GET.get("pass")
        ret = {"flag": False, "error_msg": None}
        user = authenticate(username=name, password=pwd)
        if user is not None:
            # 如果验证成功就让登录
            login(request, user)
            request.session["elearning_login"] = False
            request.session["jwfw_login"] = False
            ret["flag"] = True
            print("登陆成功")
        else:
            ret["error_msg"] = "用户名和密码错误"
            print("登陆错误")
        # else:
        #    ret["error_msg"] = "验证码错误"
        return HttpResponse(json.dumps(ret))


@csrf_exempt
def home(request):
    # print("home begin work")
    if not request.user.is_authenticated:
        return redirect('/login')
    if not login_uis(request):
        return redirect('/personal')
    if request.method == 'GET':  # 这里用于向前端传输数据用于渲染主页
        return render(request, 'home.html')


@csrf_exempt
def lesson(request):
    print("lesson begin work")
    if not request.user.is_authenticated:
        return redirect('/login')
    if not login_uis(request):
        return redirect('/personal')
    if request.method == 'GET':
        return render(request, 'lessons.html')


@csrf_exempt
def personal(request):
    # print("personal begin work")
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'GET':
        return render(request, 'personal.html')


@csrf_exempt
def course(request):
    print("course begin work")
    print(request)
    print(request.method)
    if not request.user.is_authenticated:
        return redirect('/login')
    if not login_uis(request):
        return redirect('/personal')
    if request.method == 'POST':
        course_id = request.GET.get("course_id")
        print(course_id)
        request.session["course_id"] = course_id
        print(request.session['course_id'])
        ret = {'flag': True}
        return HttpResponse(json.dumps(ret))

@csrf_exempt
def ToCourse(request):
    return render(request, 'SingleCourse.html')

@csrf_exempt
def get_schedule(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        login_uis(request)
        scheduler = get_scheduler_feedback(request.session["elearning_session"], request.session["jwfw_session"])
        ret = {}
        ret['course'] = scheduler
        ret["flag"] = True
        return JsonResponse(ret)
        # 此处需要存入数据库，后端存入

        ret = {}
        test = True
        now = datetime.datetime.now()
        if test == True:
            course_list = [
                {
                    "title": "Hey!",
                    "start": "",
                    "className": "bg-purple",
                },
                {
                    "title": "See John Deo",
                    "start": now,
                    "end": now,
                    "className": "bg-success"
                },
                {
                    "title": "Meet John Deo",
                    "start": now + 168e6,
                    "className": "bg-info",
                },
                {
                    "title": "Buy a Theme",
                    "start": now + 338e6,
                    "className": "bg-primary",
                },
            ]
            pass

        return JsonResponse(ret)


Data = [
    {
        "name": "Algorithm Assignment 3",
        "time": "2020-5-9 10:30",
        "description": "Complete 15-2.3,17.1",
        "status": 0,
        "id": 1
    },
    {
        "name": "Software Engineer homework",
        "time": "2020-5-9 18:30",
        "description": "Implement the demo website.",
        "status": 1,
        "id": 2
    },
    {
        "name": "Watch a movie",
        "time": "2020-5-9 24:00",
        "description": "",
        "status": 2,
        "id": 3
    },
    {
        "name": "DSP homwork3",
        "time": "2020-5-9 24:00",
        "description": "this is a long long long long description.for test for test for test.",
        "status": 0,
        "id": 4
    }
]


@csrf_exempt
def add_ddl_elearning(request):
    # print("%%%%%%%%%%")
    data = get_ddl_feedback(request.session["elearning_session"], request.session["jwfw_session"])
    # print("@@@@@@@@@@")
    data = data["todo"]
    print("ddl_data")
    print(data)
    account = Account.objects.get(user=request.user)
    for ddl in data:
        if not Todolist.objects.filter(account=account, name=ddl["title"]).exists():
            time = datetime.datetime.strptime(ddl["ddl"], "%Y-%m-%dT%H:%M:%SZ")
            Todolist.objects.create(account=account, name=ddl["title"], description=ddl["content"], deadline_time=time)
    todolist = account.todolist_set.all()
    print("time!!!!!!!!!!!!!")
    print(todolist[3].deadline_time)


@csrf_exempt
def get_Todaylist(request):  # Todo 连接数据库
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        ret = []
        # print("Getting todaylist!")
        # print("--------")
        login_uis(request)
        # print("********")
        add_ddl_elearning(request)
        # print("########")
        """
        if DEBUG:
            # print("abc")
            global Data
            ret = {
                "flag": True,
                "TodayList": Data
            }

            # print(ret)
            return JsonResponse(ret)
        """
        # print(request.user)
        user = Account.objects.get(user=request.user)
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        temp = user.todolist_set.all()
        todolist = user.todolist_set.filter(deadline_time__range=(now, tomorrow))
        todolist.order_by('deadline_time')

        for todo in todolist:
            now = {}
            now["name"] = todo.name
            time = todo.deadline_time
            now["time"] = time.strftime("%Y-%m-%d %H:%M")
            now["description"] = todo.description
            now["status"] = todo.status
            now["id"] = todo.todolist_id
            ret.append(now)
        ret = {"TodayList": ret}
        ret["flag"] = True
        print(ret)
        return JsonResponse(ret)


@csrf_exempt
def get_Weeklist(request):  # Todo 连接数据库
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        login_uis(request)
        add_ddl_elearning(request)
        ret = []
        # print("kaishiWeek")
        """
        if DEBUG:
            global Data
            ret = {
                "flag": True,
                "WeekList": Data
            }
            return JsonResponse(ret)
        """
        user = Account.objects.get(user=request.user)
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        nextweek = now + datetime.timedelta(days=31)
        todolist = user.todolist_set.filter(deadline_time__range=(tomorrow, nextweek))
        todolist.order_by('deadline_time')
        # print("todolist",todolist)

        for todo in todolist:
            now = {}
            now["name"] = todo.name
            time = todo.deadline_time
            now["time"] = time.strftime("%Y-%m-%d %H:%M")
            now["description"] = todo.description
            now["status"] = todo.status
            print(todo.todolist_id)
            now["id"] = todo.todolist_id
            ret.append(now)

        ret = {"WeekList": ret}
        ret["flag"] = True
        print(ret)
        return JsonResponse(ret)


@csrf_exempt
def ToCourse(request):
    return render(request, 'SingleCourse.html')


@csrf_exempt
def checkcode(request):
    if request.method == 'POST':
        ret = {}
        try:
            register = Register.objects.get(email=request.GET.get("email"))
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
        if Account.objects.filter(email=email).exists():
            ret["flag"] = False
            ret["error_msg"] = "邮箱已注册！"
            return JsonResponse(ret)
        try:
            register = Register.objects.get(email=email)
            print("try")
        except:
            register = Register(email=email)
            print("except")
        register.checksum = random.randint(1000, 9999)
        print(register.email, register.checksum)
        register.save()
        ret["checksum"] = register.checksum
        ret["flag"] = True
        return JsonResponse(ret)


@csrf_exempt
def logout_account(request):
    logout(request)
    return render(request, 'index.html')


@csrf_exempt
def check_todolist(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        ret = {}
        """
        if DEBUG:
            global Data
            switch = {0: 0, 1: 1, 2: 2}
            status = int(request.GET["status"])
            id = int(request.GET["id"])
            # print(id, status)
            # print(switch[status])
            if status not in switch:
                # print("notin")
                ret["flag"] = False
                ret["error_msg"] = "Wrong status!"
                return JsonResponse(ret)
            for i in range(len(Data)):
                if Data[i]["id"] == id:
                    Data[i]["status"] = status
            ret["flag"] = True
            return JsonResponse(ret)
        """

        id = request.GET.get("id")
        print(id)
        if not Todolist.objects.filter(todolist_id=request.GET.get("id")).exists():
            print("Error!")
            ret["flag"] = False
            ret["error_msg"] = "Todolist id doen'st exist!"
            return JsonResponse(ret)
        Todo = Todolist.objects.get(todolist_id=request.GET.get("id"))
        if Todo.account.user != request.user:
            print("Error!")
            ret["flag"] = False
            ret["error_msg"] = "Your account doesn't own this todolist!"
            return JsonResponse(ret)
        switch = {"0": 0, "1": 1, "2": 2}
        status = request.GET["status"]
        print(status)
        if status not in switch:
            print("Error!")
            ret["flag"] = False
            ret["error_msg"] = "Wrong status!"
            return JsonResponse(ret)
        Todo.status = status
        Todo.save()
        ret["flag"] = True
        return JsonResponse(ret)


@csrf_exempt
def add_ddl(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'POST':
        """
        if DEBUG:
            global Data
            new_ddl = {}
            new_ddl["name"] = request.GET["name"]
            new_ddl["time"] = request.GET["time"]
            new_ddl["description"] = request.GET["description"]
            new_ddl["id"] = len(Data) + 1
            new_ddl["status"] = 0
            Data.append(new_ddl)
            print(Data)
            ret = {}
            ret["flag"] = True
            return JsonResponse(ret)
        """
        account = Account.objects.get(user=request.user)
        todolist = Todolist(name=request.GET["name"])
        todolist.account = account
        time = datetime.datetime.strptime(request.GET["time"], "%Y-%m-%d %H:%M")
        todolist.deadline_time = time
        todolist.description = request.GET["description"]
        todolist.save()
        ret = {}
        ret["flag"] = True
        return JsonResponse(ret)


@csrf_exempt
def del_ddl(request):
    if not request.session.get('login', None):
        return redirect('/login_page/')
    if request.method == 'GET':
        test = True
        if test:
            global Data
            del_id = int(request.GET["id"])
            # 这里直接遍历了一遍
            for i in range(len(Data)):
                if Data[i]["id"] == del_id:
                    del Data[i]
                    break
            ret = {"flag": True}
            return JsonResponse(ret)


@csrf_exempt
def get_semester(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        if DEBUG:
            ret = get_lesson_feedback(request.session["elearning_session"], request.session["jwfw_session"])
            return JsonResponse(ret)


@csrf_exempt
def get_courseinfo(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        login_uis(request)
        # ret = get_courseinfo_feedback(request.session["elearning_session"], request.session["jwfw_session"],
        #                               request.session["course_id"])
        ret = {
            'name': 'COMP130011.01 算法设计与分析 Algorithm Design and Analysis',
            'description': '<div class="show-content user_content clearfix enhanced">\n' +
                           '  <h1 class="page-title">COMP30011.01 算法设计与分析   （2020春）</h1>\n' +
                           '  \n' +
                           '    \n' +
                           '  \n' +
                           '  \n' +
                           '    <p><strong>教师</strong>：朱山风&nbsp; （zhusf@fudan.edu.cn)</p>\n' +
                           '<p><strong>助教</strong>：游榕晖(<a href="mailto:19210240010@fudan.edu.cn">18110240018@fudan.edu.cn)</a>、马金辰 (<a href="mailto:19210240085@fudan.edu.cn"></a>16307130043<a href="mailto:19210240085@fudan.edu.cn">@fudan.edu.cn</a>&nbsp;主要负责PJ相关事宜)&nbsp;</p>\n' +
                           '<p><strong>时间</strong>：</p>\n' +
                           '<p class="p1">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 每周四 下午1点30分-4点10分<span class="Apple-converted-space">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span></p>\n' +
                           '<p class="p1">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;周一（双周）下午3点25分-5点05分</p>\n' +
                           '<p class="p1">&nbsp;</p>\n' +
                           '<p><strong>在线课程</strong>：学堂在线&nbsp; 算法设计与分析</p>\n' +
                           '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<a class="external" href="https://next.xuetangx.com/course/THU08091001409/1515822" target="_blank">https://next.xuetangx.com/course/THU08091001409/1515822</a></p>\n' +
                           '<p>&nbsp; <strong>教材</strong></p>\n' +
                           '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; J. Kleinberg, E. Tardos. Algorithm Design.&nbsp; &nbsp;算法设计 清华大学出版社 2007</p>\n' +
                           '<p>&nbsp;</p>\n' +
                           '<p><strong>参考书目</strong></p>\n' +
                           '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;算法导论 （殷建平等编译，机械工业出版社2013年出版）</p>\n' +
                           '<p>&nbsp; <strong style="font-family: sans-serif; font-size: 1rem;">参考课程&nbsp; &nbsp;</strong></p>\n' +
                           '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 网易公开课&nbsp; &nbsp; 算法导论</p>\n' +
                           '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://open.163.com/newview/movie/courseintro?newurl=%2Fspecial%2Fopencourse%2Falgorithms.html" class="external" target="_blank" rel="noreferrer noopener"><span>http://open.163.com/newview/movie/courseintro?newurl=%2Fspecial%2Fopencourse%2Falgorithms.html</span><span aria-hidden="true" class="ui-icon ui-icon-extlink ui-icon-inline" title="链接到外部网站。"></span><span class="screenreader-only">&nbsp;(链接到外部网站。)</span></a></p>\n' +
                           '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>\n' +
                           '  \n' +
                           '</div>'

        }
        return JsonResponse(ret)


@csrf_exempt
def get_course_detail(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        login_uis(request)
        # ret = get_course_detail_feedback(request.session["elearning_session"], request.session["jwfw_session"],
        #                                  request.session["course_id"])
        ret = {
            'name': 'COMP130011.01 算法设计与分析 Algorithm Design and Analysis',
            'docs':
                [
                    {
                        'title': '课程要求',
                        'expand': True,
                        'children': [
                            {
                                'title': '算法分析与设计第一课.pdf',
                                'urls': 'https://elearning.fudan.edu.cn/files/298742/download?download_frd=1',
                            },
                            {
                                'title': '算法分析与设计第二课.pdf',
                                'urls': "https://elearning.fudan.edu.cn/files/342954/download?download_frd=1",
                            }
                        ]
                    },
                    {
                        'title': '作业',
                        'expand': True,
                        'children': [
                            {
                                'title': '算法分析与设计习题1',
                                'urls': 'https://elearning.fudan.edu.cn/files/298744/download?download_frd=1',
                            },
                            {
                                'title': '算法分析与设计习题2',
                                'urls': "https://elearning.fudan.edu.cn/files/342955/download?download_frd=1",
                            }
                        ]
                    }

                ]
        }
        return JsonResponse(ret)


@csrf_exempt
def get_course_homework(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        login_uis(request)
        # ret = get_course_homework_feedback(request.session["elearning_session"], request.session["jwfw_session"],
        #                                    request.session["course_id"])
        ret = {
            'name': 'COMP130011.01 算法设计与分析 Algorithm Design and Analysis',
            'not_done': [
                {
                    'title': '算法设计与分析作业3',
                    'description': '<a class="instructure_file_link" title="算法设计与分析习题 3.pdf" href="https://elearning.fudan.edu.cn/files/519713/download?wrap=1">算法设计与分析习题 3.pdf</a>',
                    'content': '第三次算法与设计分析作业，具体内容见文档',
                    'ddl': '4.14日 13：30前',
                    'score': '10'
                }
            ],
            'done': [
                {
                    'title': '算法设计与分析作业2',
                    'description': '<a class="instructure_file_link" title="算法设计与分析习题 2.pdf" href="https://elearning.fudan.edu.cn/files/519713/download?wrap=1">算法设计与分析习题 2.pdf</a>',
                    'content': '第二次算法与设计分析作业，具体内容见文档',
                    'ddl': '4.6日 13：30前',
                    'score': '10',
                    'grade': 'A',
                    'comment': 'nice!',
                    'finish': True,
                    'submission': '<a href="/courses/22322/assignments/8981/submissions/14325?download=480636">\n' + '            下载 17307130254-2.pdf\n' + '          </a>'
                },
                {
                    'title': '算法设计与分析作业1',
                    'description': '<a class="instructure_file_link" title="算法设计与分析习题 1.pdf" href="https://elearning.fudan.edu.cn/files/519713/download?wrap=1">算法设计与分析习题 1.pdf</a>',
                    'content': '第一次算法与设计分析作业，具体内容见文档',
                    'ddl': '4.1日 13：30前',
                    'score': '10',
                    'grade': 'D',
                    'comment': 'where is your homework??',
                    'finish': False,
                    'submission': ''
                }
            ]
        }
        return JsonResponse(ret)


@csrf_exempt
def elearning_register(request):
    print("elearning register!")
    if not request.user.is_authenticated:
        print("elearning failed!")
        return redirect('/login_page/')
    if request.method == 'GET':
        print("elearning!")
        name = request.GET["username"]
        password = request.GET["password"]
        session, flag = login_elearning(name, password)
        account = Account.objects.get(user=request.user)
        if flag == False:
            ret = {"flag": False, "status": account.elearning_login}
            return JsonResponse(ret)
        account.elearning_name = name
        account.elearning_password = password
        account.elearning_login = True
        # print(account)
        account.save()
        ret = {"flag": True, "status": account.elearning_login}
        return JsonResponse(ret)


@csrf_exempt
def elearning_del_register(request):
    print("Elearning delete register!")
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        account = Account.objects.get(user=request.user)
        account.elearning_name = ""
        account.elearning_password = ""
        account.elearning_login = False
        account.save()
        ret = {"flag": True, "status": account.elearning_login}
        return JsonResponse(ret)


@csrf_exempt
def information(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'POST':
        account = Account.objects.get(user=request.user)
        account.email = request.GET["mail"]
        account.nickname = request.GET["name"]
        account.addr = request.GET["addr"]
        account.phone = request.GET["phone"]
        account.description = request.GET["desc"]
        account.save()
        ret = {"flag": True}
        return JsonResponse(ret)


@csrf_exempt
def picture(request):
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'POST':
        account = Account.objects.get(user=request.user)
        account.picture = request.GET["pic"]
        account.save()
        ret = {"flag": True}
        return JsonResponse(ret)


@csrf_exempt
def personal_create(request):
    print("Personal start working.")
    if not request.user.is_authenticated:
        return redirect('/login_page/')
    if request.method == 'GET':
        print("Personal create!")
        print(request.user)
        account = Account.objects.get(user=request.user)
        print(account.elearning_name, account.elearning_password, account.elearning_login)

        ret = {}
        ret["flag"] = True
        ret["status"] = account.elearning_login
        if not account.nickname:
            account.nickname = request.user
        ret["name"] = account.nickname
        ret["addr"] = account.addr
        ret["mail"] = account.email
        ret["phone"] = account.phone
        ret["desc"] = account.description
        ret["userImg"] = account.picture
        print(ret)
        return JsonResponse(ret)
