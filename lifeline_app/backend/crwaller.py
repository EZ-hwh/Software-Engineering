import requests
import urllib
import random
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import json
import re




def login_elearning(username,password):
    """
    登录并返回已经登录的会话
    :return: 已经登录的会话(session)
    """
    #设置
    #userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    login_url = "https://uis.fudan.edu.cn/authserver/login?service=https%3A%2F%2Felearning.fudan.edu.cn%2Flogin%2Fcas"
    headers = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    #新建会话
    session=requests.session()
    html=session.post(login_url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    lt=soup.find('input',{'name':'lt'})['value']
    dllt=soup.find('input',{'name':'dllt'})['value']
    execution = soup.find('input', {'name': 'execution'})['value']
    _eventId = soup.find('input', {'name': '_eventId'})['value']
    rmShown = soup.find('input', {'name': 'rmShown'})['value']
    login_data={
        'username': username, #input("请输入学号："),
        'password': password ,#input("请输入密码："),
        #'btn':'',
        'lt': lt,
        'dllt': dllt,
        'execution': execution,
        '_eventId': _eventId,
        'rmShown': rmShown
    }
    #登录
    response=session.post(login_url,headers=headers,data=login_data)
    print(response.url)
    flag = False
    if response.url=='https://elearning.fudan.edu.cn/dash?login_success=1':
        print('登录成功！')
        flag = True
    return session, flag

def login_jwfw(username,password):
    """
    登录并返回已经登录的会话
    :return: 已经登录的会话(session)
    """
    #设置
    #userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    login_url = "https://uis.fudan.edu.cn/authserver/login?service=http%3A%2F%2Fjwfw.fudan.edu.cn%2Feams%2Flogin.action"
    headers = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    #新建会话
    session=requests.session()
    html=session.post(login_url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    lt=soup.find('input',{'name':'lt'})['value']
    dllt=soup.find('input',{'name':'dllt'})['value']
    execution = soup.find('input', {'name': 'execution'})['value']
    _eventId = soup.find('input', {'name': '_eventId'})['value']
    rmShown = soup.find('input', {'name': 'rmShown'})['value']
    login_data={
        'username': username, #input("请输入学号："),
        'password': password ,#input("请输入密码："),
        #'btn':'',
        'lt': lt,
        'dllt': dllt,
        'execution': execution,
        '_eventId': _eventId,
        'rmShown': rmShown
    }
    #登录
    response=session.post(login_url,headers=headers,data=login_data)
    print(response.url)
    response=session.get(url="http://jwfw.fudan.edu.cn/eams/login.action",headers=headers)
    print(response.url)
    flag = False
    if response.url=='https://jwfw.fudan.edu.cn/eams/home.action':
        print('登录成功！')
        flag = True
    return session, flag

def get_course_mainpage(session,course_id):
    """
    获取课程主页
    """
    #　设置头部
    headers = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    html = session.get("https://elearning.fudan.edu.cn/courses/"+course_id,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    #print(soup)
    title = soup.find("li",id="crumb_course_"+course_id).find("span").get_text()
    print(title)
    description = soup.find_all('script')[3].get_text()
    d = json.loads(description[description.rfind('ENV')+6:description.rfind(';')])
    #print(d)
    try:
        d1 = d['WIKI_PAGE']
        return title,d1['body']
    except:
        return title,""
    
    #print(description[description.rfind('ENV')+6:description.rfind(';')])
    #print(d1['title'])
    #print(d1['body'])

def get_document(session,diction):
    #　设置头部
    headers = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    # html = session.get(url = url,headers=headers).text
    # #print(url)
    # ret = []
    # if html == "while(1);[]":
    #     return ret 

    # html = html.replace("null","None").replace("false","False").replace("true","True")
    # files = eval(html[9:])
    # if isinstance(files,dict):
    #     files = [files]
    # print(files)
    #print(d["files_url"])
    #print(d["folders_url"])
    ret = []
    html = session.get(url=diction["folders_url"],headers=headers).text
    #print(html)
    html = html.replace("null","None").replace("false","False").replace("true","True")
    files = eval(html[9:])
    #循环读取文件夹
    for f in files:
        folder = {"title":f["name"],"expand":True,"urls":""}
        print(f["folders_url"])
        folder["children"] = []
        folder["children"] = get_document(session,f)
        ret.append(folder)

    #获取该目录下的文件表格
    html = session.get(url=diction["files_url"],headers=headers).text
    html = html.replace("null","None").replace("false","False").replace("true","True")
    #print(html)
    files = eval(html[9:]) #将文件变成list，每个元素都是一个文件信息的字典
    for f in files:
        #t = session.get(url=f['url'],headers=headers).text
        #print(t)
        #print(f["display_name"])
        file = {"title":f["display_name"],"expand":False,"urls":f['url'],"children":[]}
        ret.append(file)
    return ret

def get_homework(session,url):
    #　设置头部
    headers = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    #url = url+'/files'
    html = session.get(url = url,headers=headers).text
    html = html.replace("null","None").replace("false","False").replace("true","True")
    #print(html)
    #print(url)
    homeworks = eval(html[9:])[0]["assignments"]
    dones = []
    not_dones = []
    for item in homeworks:
        a = {}
        homework_url = item["html_url"]
        html = session.get(url=homework_url,headers=headers).text
        soup = BeautifulSoup(html,"lxml")
        a["title"] = item["name"]
        a["content"] = soup.find("div",class_="description user_content student-version").get_text()
        a["description"]=""
        #print(description)
        a["ddl"] = item["due_at"]
        a["score"] = item["points_possible"]
        #下面用于提交作业后信息的采集
        if soup.find("div",class_="details"):
            a["comment"]=soup.find("div",class_="comments module").get_text()
            a['grade']=soup.find("div",class_="module").get_text()
            a['finish']=True
            a["submission"]=soup.find("div",class_="details").find_all("div")[3]
            dones.append(a)
        else:
            not_dones.append(a)
        #if item['has_submitted_submissions']:
        #    a[]
    return dones,not_dones

def get_course(session):
    """
        获取用户所有的课程
    """
    headers = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    html = session.get(url = "https://elearning.fudan.edu.cn/courses",headers=headers).text
    soup = BeautifulSoup(html,"lxml")
    raw_course = soup.find_all("tr",class_="course-list-table-row")
    all_course = []
    for i in raw_course:
        course = {}
        #print(i)
        course["name"]=i.find("span",class_="name").string.strip()
        if i.find("td",class_="course-list-no-left-border course-list-term-column"):
            course["term"]=i.find("td",class_="course-list-no-left-border course-list-term-column").text
        else:
            course["term"]=None
        if i.find("a"):
            course["id"]=i.find("a")["href"]
        else:
            course["id"]=None
        if i.find("td",class_="course-list-no-left-border course-list-term-column"):
            course["term"]=i.find("td",class_="course-list-no-left-border course-list-term-column").string
        else:
            course['term']=None
        all_course.append(course)
    return(all_course)

def get_coursedesk(session): #读取课程表
    headers = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    html = session.get(url = "https://jwfw.fudan.edu.cn/eams/courseTableForStd.action",headers=headers).text

    pos = re.search('bg.form.addInput',html).span()[1]
    p = re.search(u"\d+",html[pos:]).span()
    s,e = p[0],p[1]
    print(p)
    post_data={
        "ignoreHead": 1,
        "setting.kind": "std",
        "startWeek": 1,
        "project.id": 1,
        "semester.id": 325,
        "ids": html[pos+p[0]:pos+p[1]],
    }
    html = session.post(data=post_data,url = "https://jwfw.fudan.edu.cn/eams/courseTableForStd!courseTable.action",headers=headers).text
    #print(html)
    soup = BeautifulSoup(html,"lxml")
    scip = str(soup.find_all("script")[-2]).replace("\t","").split("\n")
    i = 6
    timezones = {}
    while i<len(scip):
        if scip[i][:8] == 'activity':
            s = scip[i].split(",")[3].replace('"',"").split("(")[0]
            #print(s)
        if scip[i][:5] == 'index':
            if s not in timezones.keys():
                timezones[s] = []
            res = re.findall("\d+",scip[i])
            #print(res)
            timezones[s].append(res[0]+'-'+res[1])
        i = i+1
    #print(timezones)    
    return timezones

def get_scheduler_feedback(session1,session2):
    course1 = get_course(session1)
    course2 = get_coursedesk(session2)
    res = []
    for key in course2.keys():
        r = {}
        r["name"]=key
        print(key)
        for item in course1:
            if key in item["name"]:
                if item["id"]:
                    _, r["description"] = get_course_mainpage(session1,item["id"])
                else:
                    r["description"] = ""
                break
        r["time"]=course2[key]
        res.append(r)
    print(res)
    return res

#登录并获得登录的会话
# session1 = login_elearning(username,password)
# session2 = login_jwfw(username,password)

def get_course_homework_feedback(session1,session2,id):
    name,_ = get_course_mainpage(session1,id)
    dones,not_dones = get_homework(session1,url="https://elearning.fudan.edu.cn/api/v1/courses/"+id+"/assignment_groups?exclude_response_fields%5B%5D=description&exclude_response_fields%5B%5D=rubric&include%5B%5D=assignments&include%5B%5D=discussion_topic&override_assignment_dates=true&per_page=50")
    ret = {}
    ret["name"] = name
    ret["done"] = dones
    ret["not_done"] = not_dones
    print(ret)
    return ret

def get_course_detail_feedback(session1,session2,id):
    name,_ = get_course_mainpage(session1,id)
    url = "https://elearning.fudan.edu.cn/api/v1/courses/"+id+"/folders/root"
    headers = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    html = session1.get(url = url,headers=headers).text
    #print(url)
    ret = {}
    ret["name"] = name
    ret["docs"] = []
    if html == "while(1);[]":
        return ret 

    html = html.replace("null","None").replace("false","False").replace("true","True")
    files = eval(html[9:])
    print(files)
    ret["docs"] = get_document(session1,files)
    #还未开始
    print(ret)
    return ret

def get_courseinfo_feedback(session1,session2,id):
    title, description = get_course_mainpage(session1,id)
    return {"name":title,"description":description}

def test():
    a = []
    a1=b1=c1=d1=e1=f1=0
    b = []
    c = []
    d = []
    e = []
    f = []
    for i in course:
        if i["term"]:
            print(i["term"])
        else:
            print()
        if i["term"] == "\n        2019-2020学年第二学期\n      ":
            a1 = a1 + 1
            a.append({"name":i["name"],"index":a1})
        if i["term"] == "\n        2019-2020学年第一学期\n      ":
            b1 = b1 + 1
            b.append({"name":i["name"],"index":b1})
        if i["term"] == "\n        2018-2019学年第二学期\n      ":
            c1 = c1 + 1
            c.append({"name":i["name"],"index":c1})
        if i["term"] == "\n        2018-2019学年第一学期\n      ":
            d1 = d1 + 1
            d.append({"name":i["name"],"index":d1})
        if i["term"] == "\n        2017-2018学年第二学期\n      ":
            e1 = e1 + 1
            e.append({"name":i["name"],"index":e1})
        if i["term"] == "\n        2017-2018学年第一学期\n      ":
            f1 = f1 + 1
            f.append({"name":i["name"],"index":f1})
    ans = []
    ans.append({"lesson":a})
    ans.append({"lesson":b})
    ans.append({"lesson":c})
    ans.append({"lesson":d})
    ans.append({"lesson":e})
    ans.append({"lesson":f})
    print(ans)
#get_course_detail_feedback(session1,session2,"22474")
# get_course_homework_feedback(session1,session2,"22322")
#get_scheduler_feedback(session1,session2)
#url = "https://elearning.fudan.edu.cn/courses/22474"
#title, body = get_course_mainpage(session,url)
#get_document(session,"https://elearning.fudan.edu.cn/api/v1/courses/22474/folders/root")
#get_homework(session,"https://elearning.fudan.edu.cn/api/v1/courses/22474/assignment_groups?exclude_response_fields%5B%5D=description&exclude_response_fields%5B%5D=rubric&include%5B%5D=assignments&include%5B%5D=discussion_topic&override_assignment_dates=true&per_page=50")
#course = get_course(session1)
#print(course)