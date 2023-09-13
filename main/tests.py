import json
import xml.etree.ElementTree as ET
from http import HTTPStatus

from django.http import HttpResponse
from django.test import Client, TestCase

from .models import Product


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
                "name": "Product A",
                "price": 42,
                "description": "A test product",
            },
        )
        self.assertRedirects(response, "/", response.status_code, HTTPStatus.OK)

    def test_show_xml_returns_ok(self):
        # Setup
        sample_product: Product = Product()
        sample_product.name = "Product A"
        sample_product.price = 42
        sample_product.description = "A test product"
        sample_product.save()

        # Exercise
        response: HttpResponse = Client().get("/xml/1")

        # Verify
        self.assertEquals(response.status_code, HTTPStatus.OK)

        # Cleanup
        sample_product.delete()

    def test_show_xml_produces_valid_xml(self):
        # Setup
        sample_product: Product = Product()
        sample_product.name = "Product A"
        sample_product.price = 42
        sample_product.description = "A test product"
        sample_product.save()

        # Exercise
        response: HttpResponse = Client().get("/xml/1")

        # Verify
        try:
            # TODO: The lines xml_data and so on were generated using ChatGPT.
            #       Verify if the statement is valid and current!
            xml_data = ET.fromstring(response.content)
            # TODO: Add XML validation logic
        except ET.ParseError as error:
            self.fail(f"XML parsing error: {error}")

        # Cleanup
        sample_product.delete()

    def test_show_json_returns_ok(self):
        # Setup
        sample_product: Product = Product()
        sample_product.name = "Product A"
        sample_product.price = 42
        sample_product.description = "A test product"
        sample_product.save()

        # Exercise
        response: HttpResponse = Client().get("/json/1")

        # Verify
        self.assertEquals(response.status_code, HTTPStatus.OK)

        # Cleanup
        sample_product.delete()

    def test_show_json_produces_valid_json(self):
        # Setup
        sample_product: Product = Product()
        sample_product.name = "Product A"
        sample_product.price = 42
        sample_product.description = "A test product"
        sample_product.save()

        # Exercise
        response: HttpResponse = Client().get("/json/1")

        # Verify
        try:
            # TODO: The lines json_data and so on were generated using ChatGPT.
            #       Verify if the statement is valid and current!
            json_data = json.loads(response.content.decode("utf-8"))
            # TODO: Add JSON validation logic
        except json.JSONDecodeError as error:
            self.fail(f"JSON parsing error: {error}")

        # Cleanup
        sample_product.delete()
