from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.



def index(request):
    context = {}
    return render(request, 'index.html', context)

def demo(request):
    return HttpResponse('demo page')

def contact_us(request):
    print("test")
    return HttpResponse('demo page')
    # return redirect('/')
