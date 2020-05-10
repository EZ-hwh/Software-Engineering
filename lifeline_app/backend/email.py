from django.core.mail import send_mail,send_mass_mail
import random

def send_my_email(email,checksum):
    title = 'lifeline_app验证码'
    msg = '欢迎注册Lifeline_app,您的验证码是'+str(checksum)+'请尽快完成账号验证'
    email_from = 'lifeline_app@126.com'
    reciever = [
        email
    ]
    # 发送邮件
    send_mail(title, msg, email_from, reciever)


def send_email_v1(req):#邮件中发送页面
    title = "美团骑手offer"
    msg = " "
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3207196028@qq.com'
    ]
    # 加载模板
    template = loader.get_template('email.html')
    # 渲染模板
    html_str = template.render({"msg": "123456"})
    print(html_str)
    # 发送邮件
    send_mail(title, msg, email_from, reciever, html_message=html_str)

