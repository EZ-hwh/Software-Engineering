from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from django.test import Client
from django.utils.functional import cached_property
from django.http import HttpRequest
from rest_framework.test import APITestCase as BaseAPITestCase
from importlib import import_module


# Create your tests here.

class APITestCase(BaseAPITestCase):
    @staticmethod
    def create_session():
        engine = import_module(settings.SESSION_ENGINE)
        session = engine.SessionStore()
        session.save()
        return session

    @cached_property
    def session(self):
        return self.create_session()

    def save_session(self):
        self.session.save()
        self.save_cookie(
            name=settings.SESSION_COOKIE_NAME,
            value=self.session.session_key,
            expires=None
        )

    def save_cookie(self, name, value, **params):
        self.client.cookies[name] = value
        self.client.cookies[name].update({
            k.replace('_', '-'): v
            for k, v in params.items()
        })

    def login(self, user):
        """登录用户，用于通过权限校验"""
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        request = self.make_request()
        login(request, user)
        request.user = user
        self.save_session()

    def make_request(self, user=None, auth=None, method=None):
        request = HttpRequest()
        if method:
            request.method = method
        request.META['REMOTE_ADDR'] = '127.0.0.1'
        request.META['SERVER_NAME'] = 'testserver'
        request.META['SERVER_PORT'] = 80
        request.REQUEST = {}

        # order matters here, session -> user -> other things
        request.session = self.session
        request.auth = auth
        request.user = user or AnonymousUser()
        request.is_superuser = lambda: request.user.is_superuser
        request.successful_authenticator = None
        return request


class MyAppTestsLogged(APITestCase):
    def setUp(self):
        super(MyAppTestsLogged, self).setUp()
        self.user = User.objects.create_user(username='ystt', password="Yushutian26", email="897358819@qq.com") # 创建测试用例用户
        self.login(self.user) # 模拟登录状态

    def test_Course_LoggedNoUIS(self):
        response = self.client.post('/course', data={'course_id': "/course/23223"})
        print(response.content)
        self.assertEqual(response.content, b'')

    def test_Course_LoggedUIS(self):
        response = self.client.post('/course', data={'course_id': "/course/23223"})
        print(response.content)
        self.assertEqual(response.content, b'{"flag": true}')

    def test_login_LoggedIn(self):
        response = self.client.post('/login')  # 进行登录
        print(response.content)
        self.assertEqual(response.content, b'')  # 检查返回内容

    def test_reg_LoggedIn(self):
        response = self.client.post('/register')  # 进行注册
        print(response.content)
        self.assertEqual(response.content, b'Already logged in.')  # 检查返回内容


class MyAppTests(APITestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.user = User.objects.create_user(username='ystt', password="Yushutian26")

    def test_Course_NotLogged(self):
        response = self.client.post('/course', data={'course_id': "/course/23223"})
        print(response.content)
        self.assertEqual(response.content, b'')

    def test_login_Right(self):
        response = self.client.post('/login', data={'name': "ystt", 'pass': "Yushutian26"})
        print(response.content)
        self.assertEqual(response.content, b'{"flag": true, "error_msg": null}')

    def test_login_Wrong(self):
        response = self.client.post('/login', data={'name': "ystt", 'pass': "Yushutian"})
        print(response.content)
        self.assertEqual(response.content, b'{"flag": false, "error_msg": "Wrong name or password"}')

    def test_reg_NameIn(self):
        response = self.client.post('/register', data={'name': "ystt", 'pass': "Yushutian"})
        print(response.content)
        self.assertEqual(response.content, b'{"flag": false, "error_msg": "same user has been registered"}')

    def test_reg_NameNotIn(self):
        response = self.client.post('/register', data={'name': "ystttttt", 'pass': "Yushutian"})
        print(response.content)
        self.assertEqual(response.content, b'{"flag": true, "error_msg": null}')
