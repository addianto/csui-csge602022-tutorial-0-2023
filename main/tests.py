from http import HTTPStatus
from django.test import TestCase, Client
from django.http import HttpResponse


class MainAppTest(TestCase):
    def test_show_main_returns_ok(self):
        response: HttpResponse = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_show_main_uses_correct_template(self):
        response: HttpResponse = Client().get("/")
        self.assertTemplateUsed(response, "main.html")

    def test_create_product_returns_ok(self):
        response: HttpResponse = Client().get("/create-product")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_product_uses_correct_template(self):
        response: HttpResponse = Client().get("/create-product")
        self.assertTemplateUsed(response, "create_product.html")

    def test_create_product_redirects_when_success(self):
        response: HttpResponse = Client().post(
            "/create-product",
            data={
                "name": "Product",
                "price": 42,
                "description": "A test product",
            },
        )
        self.assertRedirects(response, "/", response.status_code, HTTPStatus.OK)
