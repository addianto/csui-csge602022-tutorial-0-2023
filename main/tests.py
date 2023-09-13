from django.test import TestCase, Client
from django.http import HttpResponse


class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response: HttpResponse = Client().get("/main/")
        self.assertEquals(response.status_code, 200)

    def test_main_using_correct_template(self):
        response: HttpResponse = Client().get("/main/")
        self.assertTemplateUsed(response, "main.html")
