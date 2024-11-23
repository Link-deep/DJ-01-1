from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'caption':"NINTENDO"})


def contact(request):
    data = {
        'caption': "NINTENDO"
    }

    return render(request, 'main/contact.html', data)

def game(request):
    data = {
        'caption': "NINTENDO"
    }

    return render(request, 'main/game.html', data)



def suppliers(request):
    data = {
        'caption': "NINTENDO"
    }
    return render(request, 'main/suppliers.html', data)


def privacy_policy(request):
    data = {
        'caption': "NINTENDO"
    }

    return render(request, 'main/privacy-policy.html', data)

def terms_of_service(request):
    data = {
        'caption': "NINTENDO"
    }

    return render(request, 'main/terms-of-service.html', data)


def test(request):
    return HttpResponse("<h1>Тестовая страница </h1>")


