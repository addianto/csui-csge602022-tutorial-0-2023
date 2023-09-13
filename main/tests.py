from http import HTTPStatus
from django.test import TestCase, Client
from django.http import HttpResponse


class MainAppTest(TestCase):
    def test_main_url_is_exist(self):
        response: HttpResponse = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_main_using_correct_template(self):
        response: HttpResponse = Client().get("/")
        self.assertTemplateUsed(response, "main.html")
