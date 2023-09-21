from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from main.forms import ProductForm
from main.models import Product


def show_main(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()

    context: dict = {
        "name": "The One and Only: Rickey Astley",
        "class": "PBP Int.",
        "products": products,
    }

    return render(request, "main.html", context)


def create_product(request: HttpRequest) -> HttpResponse:
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:show_main"))

    context: dict = {
        "form": form,
    }

    return render(request, "create_product.html", context)


def show_xml(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()

    return HttpResponse(
        serializers.serialize("xml", products), content_type="application/xml"
    )


def show_json(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()

    return HttpResponse(
        serializers.serialize("json", products), content_type="application/json"
    )


def show_xml_by_id(request: HttpRequest, id: int) -> HttpResponse:
    # See: https://docs.djangoproject.com/en/4.2/topics/db/queries/#retrieving-a-single-object-with-get
    try:
        product = Product.objects.get(pk=id)
        return HttpResponse(
            serializers.serialize("xml", [product]), content_type="application/xml"
        )
    except ObjectDoesNotExist as product_not_found:
        return HttpResponseRedirect(reverse("main:show_xml"))


def show_json_by_id(request: HttpRequest, id: int) -> HttpResponse:
    # See: https://docs.djangoproject.com/en/4.2/topics/db/queries/#retrieving-a-single-object-with-get
    try:
        product = Product.objects.get(pk=id)
        return HttpResponse(
            serializers.serialize("json", [product]), content_type="application/json"
        )
    except ObjectDoesNotExist as product_not_found:
        return HttpResponseRedirect(reverse("main:show_json"))


def register(request: HttpRequest) -> HttpResponse:
    form = UserCreationForm()

    if request.method == "POST":
        form: UserCreationForm = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")

    context: dict = {
        "form": form,
    }

    return render(request, "register.html", context)


def login_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username: str = request.POST.get("username")
        password: str = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main:show_main")
        else:
            messages.info(
                request, "Sorry, incorrect username or password. Please try again."
            )

    context: dict = {}

    return render(request, "login.html", context)
