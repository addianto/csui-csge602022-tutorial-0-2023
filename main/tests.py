import json
import xml.etree.ElementTree as ET
from http import HTTPStatus

from django.http import HttpResponse
from django.test import Client, TestCase

from .models import Product


class MainAppTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_one = Product.objects.create(
            name="Product One", price=10, description="A test product called One"
        )
        cls.product_two = Product.objects.create(
            name="Product Two", price=20, description="A test product called Two"
        )
        cls.product_three = Product.objects.create(
            name="Product Three", price=30, description="A test product called Three"
        )

    def test_show_main_returns_ok(self):
        response: HttpResponse = Client().get("/")
        self._is_status_ok(response)

    def test_show_main_uses_correct_template(self):
        response: HttpResponse = Client().get("/")
        self.assertTemplateUsed(response, "main.html")

    def test_create_product_returns_ok(self):
        response: HttpResponse = Client().get("/create-product")
        self._is_status_ok(response)

    def test_create_product_uses_correct_template(self):
        response: HttpResponse = Client().get("/create-product")
        self.assertTemplateUsed(response, "create_product.html")

    def test_create_product_redirects_when_success(self):
        response: HttpResponse = Client().post(
            "/create-product",
            data={
                "name": "Product Test",
                "price": 42,
                "description": "A test product",
            },
        )
        self.assertRedirects(response, "/", response.status_code, HTTPStatus.OK)

    def test_show_xml_returns_ok(self):
        # Setup
        # Done by setUpTestData()

        # Exercise
        response: HttpResponse = Client().get("/xml")

        # Verify
        self._is_status_ok(response)

        # Cleanup
        # Cleaned by Django testing classes

    def test_show_xml_produces_valid_xml(self):
        # Setup
        # Done by setUpTestData()

        # Exercise
        response: HttpResponse = Client().get("/xml")

        # Verify
        try:
            # TODO: The lines xml_data and so on were generated using ChatGPT.
            #       Verify if the statement is valid and current!
            xml_data = ET.fromstring(response.content)
            # TODO: Add XML validation logic
        except ET.ParseError as error:
            self.fail(f"XML parsing error: {error}")

        # Cleanup
        # Cleaned by Django testing classes

    def test_show_json_returns_ok(self):
        # Setup
        # Done by setUpTestData()

        # Exercise
        response: HttpResponse = Client().get("/json")

        # Verify
        self._is_status_ok(response)

        # Cleanup
        # Cleaned by Django testing classes

    def test_show_json_produces_valid_json(self):
        # Setup
        # Done by setUpTestData()

        # Exercise
        response: HttpResponse = Client().get("/json")

        # Verify
        try:
            # TODO: The lines json_data and so on were generated using ChatGPT.
            #       Verify if the statement is valid and current!
            json_data = json.loads(response.content.decode("utf-8"))
            # TODO: Add JSON validation logic
        except json.JSONDecodeError as error:
            self.fail(f"JSON parsing error: {error}")

        # Cleanup
        # Cleaned by Django testing classes

    def test_show_xml_by_id_returns_ok(self):
        # Exercise
        response: HttpResponse = Client().get("/xml/1")

        # Verify
        self._is_status_ok(response)

    def test_show_json_by_id_returns_ok(self):
        # Exercise
        response: HttpResponse = Client().get("/json/1")

        # Verify
        self._is_status_ok(response)

    def _is_status_ok(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_register_returns_ok(self):
        response: HttpResponse = Client().get("/register")

        self._is_status_ok(response)
