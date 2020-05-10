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
    privilege = models.IntegerField(default=1) # 账户等级，初步打算老师和学生账户,老师是0，学生是1
    photo = models.ImageField(default="",upload_to="",null=True) # 默认无照片的路径，以及上传图片的路径

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
    account_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    deadline_time = models.DateTimeField()
    homework = models.ForeignKey(Homework,on_delete=models.CASCADE,null=True)
    scheduler = models.ForeignKey(Scheduler,on_delete=models.CASCADE)

class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True) #验证邮箱
    checksum = models.TextField() #验证码
    time = models.DateTimeField(auto_now = True) #用于设置验证时间

class Takeclass(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    privilege = models.IntegerField() #用于表示授课还是听课关系
