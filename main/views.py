from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def show_main(request: HttpRequest) -> HttpResponse:
    context: dict = {
        "name": "The One and Only: Rickey Astley",
        "class": "PBP Int.",
    }

    return render(request, "main.html", context)
