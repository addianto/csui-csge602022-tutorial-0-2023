from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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

    return HttpResponse(serializers.serialize("xml", products), content_type="application/xml")
