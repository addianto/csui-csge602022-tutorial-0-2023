import json
import xml.etree.ElementTree as ET
from http import HTTPStatus

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase

from .models import Product


class MainAppTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user: User = User.objects.create_user(
            username="test_user", password="test_pass"
        )

        cls.product_one = Product.objects.create(
            name="Product One",
            price=10,
            description="A test product called One",
            user=test_user,
        )
        cls.product_two = Product.objects.create(
            name="Product Two",
            price=20,
            description="A test product called Two",
            user=test_user,
        )
        cls.product_three = Product.objects.create(
            name="Product Three",
            price=30,
            description="A test product called Three",
            user=test_user,
        )

    def setUp(self):
        self.client.login(username="test_user", password="test_pass")

    def tearDown(self):
        self.client.logout()

    def test_show_main_returns_ok(self):
        response: HttpResponse = self.client.get("/")
        self._is_status_ok(response)

    def test_show_main_uses_correct_template(self):
        response: HttpResponse = self.client.get("/")
        self.assertTemplateUsed(response, "main.html")

    def test_create_product_returns_ok(self):
        response: HttpResponse = self.client.get("/create-product")
        self._is_status_ok(response)

    def test_create_product_uses_correct_template(self):
        response: HttpResponse = self.client.get("/create-product")
        self.assertTemplateUsed(response, "create_product.html")

    def test_create_product_redirects_when_success(self):
        response: HttpResponse = self.client.post(
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
        response: HttpResponse = self.client.get("/xml")

        # Verify
        self._is_status_ok(response)

        # Cleanup
        # Cleaned by Django testing classes

    def test_show_xml_produces_valid_xml(self):
        # Setup
        # Done by setUpTestData()

        # Exercise
        response: HttpResponse = self.client.get("/xml")

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
        response: HttpResponse = self.client.get("/json")

        # Verify
        self._is_status_ok(response)

        # Cleanup
        # Cleaned by Django testing classes

    def test_show_json_produces_valid_json(self):
        # Setup
        # Done by setUpTestData()

        # Exercise
        response: HttpResponse = self.client.get("/json")

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
        response: HttpResponse = self.client.get("/xml/1")

        # Verify
        self._is_status_ok(response)

    def test_show_json_by_id_returns_ok(self):
        # Exercise
        response: HttpResponse = self.client.get("/json/1")

        # Verify
        self._is_status_ok(response)

    def test_register_returns_ok(self):
        response: HttpResponse = self.client.get("/register")
        self._is_status_ok(response)

    def test_register_uses_correct_template(self):
        response: HttpResponse = self.client.get("/register")
        self.assertTemplateUsed(response, "register.html")

    def _is_status_ok(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_register_returns_ok(self):
        response: HttpResponse = self.client.get("/register")

        self._is_status_ok(response)
