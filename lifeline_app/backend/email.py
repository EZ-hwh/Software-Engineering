from django.core.mail import send_mail

def send_my_email(email,code):
    title = "lifeline_app验证码"
    msg = "欢迎注册Lifeline_app，你的验证码是"+str(code)+"，请尽快完成账号验证。"
    email_from = 'lifeline_app@126.com'
    receiver = [
        email
    ]
    # 发送邮件
    send_mail(title, msg, email_from, receiver)