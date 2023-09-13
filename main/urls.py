from django.urls import path

from main.views import create_product, show_main, show_xml, show_json

app_name = "main"  # pylint: disable=invalid-name
urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product", create_product, name="create_product"),
    path("xml", show_xml, name="show_xml"),
    path("json", show_json, name="show_json"),
]
