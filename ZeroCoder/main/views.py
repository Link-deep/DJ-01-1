from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the main index.</h1>")


def contact(request):
    return HttpResponse("<h1>Страница с контактами </h1>")


def test(request):
    return HttpResponse("<h1>Тестовая страница </h1>")


def data(request):
    return HttpResponse("<h1>страница data </h1>")