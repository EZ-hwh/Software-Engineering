from django.test import TestCase, Client

# Create your tests here.

class MyAppTests(TestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.client = Client(enforce_csrf_checks=True)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
