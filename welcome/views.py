from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.



def index(request):
    context = {'home': 1}
    return render(request, 'index.html', context)


def contact_us(request):
    context = {'contact_us': 1}
    return render(request, 'contact-us.html', context)


def register(request):
    context = {'register': 1}
    return render(request, 'register.html', context)

def login(request):
    context = {'login': 1}
    return render(request, 'login.html', context)


def logout(request):
    context = {}
    return redirect('/')


# Testing Purpose

def test(request):
    context = {'test': 1}
    return render(request, 'test.html', context)


def demo(request):
    return HttpResponse('demo page')