from django.urls import path

from main.views import (
    create_product,
    create_product_ajax,
    login_user,
    logout_user,
    register,
    show_json,
    show_json_by_id,
    show_main,
    show_xml,
    show_xml_by_id,
)

app_name = "main"  # pylint: disable=invalid-name
urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product", create_product, name="create_product"),
    path("xml", show_xml, name="show_xml"),
    path("json", show_json, name="show_json"),
    path("xml/<int:id>", show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>", show_json_by_id, name="show_json_by_id"),
    path("register", register, name="register"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),
    path("create-product-ajax", create_product_ajax, name="create_product_ajax"),
]
