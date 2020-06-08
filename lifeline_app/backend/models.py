from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    """
    用户信息表
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    email = models.EmailField(null=True) # 邮箱是否能为空？
    gender = models.CharField(max_length=2,null=True) # 键值只有三种取值：M,F,N
    nickname = models.CharField(max_length=50) # 用户自己修改的昵称
    #privilege = models.IntegerField(default=1) # 账户等级，初步打算老师和学生账户,老师是0，学生是1
    elearning_name = models.CharField(max_length=15,null=True)
    elearning_password = models.CharField(max_length=20,null=True)
    elearning_login = models.BooleanField(default=False)
    phone = models.CharField(max_length=50, null=True)
    addr = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    picture = models.CharField(max_length=50, default="/static/img/user0.png")

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50,default='abc') #课程名称
    description = models.TextField(null=True) # 课程简介

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    message = models.TextField(null=True)
    time = models.DateTimeField() # 公告发布时间，不允许为空

class Homework(models.Model):
    homework_id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)  # 
    message = models.TextField(null=True) # 作业细节
    release_time = models.DateTimeField() # 作业发布时间
    deadline_time = models.DateTimeField() # 作业截止时间

class Scheduler(models.Model):
    scheduler_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    message = models.TextField(null=True)

class Time(models.Model): #描述上课或者自定义事项的时间
    time_id = models.AutoField(primary_key=True)
    course_time = models.CharField(max_length=10, default = '0-0')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    scheduler = models.ForeignKey(Scheduler, on_delete=models.CASCADE)

class Timezone(models.Model): #时间段
    timezone_id = models.AutoField(primary_key=True)
    begin_time = models.TimeField()
    end_time = models.TimeField()

class Todolist(models.Model):
    todolist_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    deadline_time = models.DateTimeField()
    homework = models.ForeignKey(Homework,on_delete=models.CASCADE,null=True)
    scheduler = models.ForeignKey(Scheduler,on_delete=models.CASCADE,null=True)
    status = models.IntegerField(default=0) # 0代表未完成，1代表已完成，2代表过期

class Register(models.Model):
    email = models.EmailField(primary_key=True) #验证邮箱
    checksum = models.TextField(null=True) #验证码
    time = models.DateTimeField(auto_now = True) #用于设置验证时间

class Takeclass(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    privilege = models.IntegerField() #用于表示授课还是听课关系
