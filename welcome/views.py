# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def demo(request):
    return HttpResponse('demo page')
