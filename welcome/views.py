from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    context = {}

    return render(request, 'index.html', context)

def demo(request):
    return HttpResponse('demo page')
