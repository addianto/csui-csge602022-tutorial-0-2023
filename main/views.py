import datetime
from http import HTTPStatus

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from main.forms import ProductForm
from main.models import Product


@login_required(login_url="/login")
def show_main(request: HttpRequest) -> HttpResponse:
    products = Product.objects.filter(user=request.user)

    context: dict = {
        "name": request.user.username,
        "class": "PBP Int.",
        "products": products,
        # This conditional is not required if @login_required works properly
        # Nevertheless, it is still a good practice to check for any input coming from user
        # Even though not explicitly stated, cookie is a part of input transmitted from user/cient!
        "last_login": request.COOKIES["last_login"]
        if "last_login" in request.COOKIES.keys()
        else "",
    }

    return render(request, "main.html", context)


@login_required(login_url="/login")
def create_product(request: HttpRequest) -> HttpResponse:
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product: Product = form.save(commit=False)
        product.user = request.user
        product.save()
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
    form: UserCreationForm = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:show_main")

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
            response: HttpResponse = redirect("main:show_main")
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(
                request, "Sorry, incorrect username or password. Please try again."
            )

    context: dict = {}

    return render(request, "login.html", context)


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    response: HttpResponse = redirect("main:login")
    response.delete_cookie("last_login")
    return response


@login_required(login_url="/login")
def edit_product(request: HttpRequest, id: int) -> HttpResponse:
    # Get product by ID
    # Immediately throw HTTP 404 if object not found
    product: Product = get_object_or_404(Product, pk=id)

    # If the request is POST, then use the submitted data to populate fields in the form
    # Otherwise, use the found Product data to populate the fields instead
    form: ProductForm = ProductForm(request.POST or None, instance=product)

    # Self-explanatory
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context: dict = {
        "form": form,
    }

    return render(request, "edit_product.html", context)


def handle_custom_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, "404.html", context={}, status=HTTPStatus.NOT_FOUND)
