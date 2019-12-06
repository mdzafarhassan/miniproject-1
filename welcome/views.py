from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.


def index(request):
    context = {'home': 1}
    return render(request, 'index.html', context)


def contact_us(request):
    context = {'contact_us': 1}
    return render(request, 'contact-us.html', context)


def register(request):
    context = {'register': 1}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        
        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                print('Registration Completed')
                return redirect('/')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
        
        

        return redirect('/')        
    else:
        return render(request, 'register.html', context)


def login(request):
    context = {'login': 1}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html', context)


def logout(request):
    context = {}
    auth.logout(request)
    return redirect('/')



# Testing Purpose

def test(request):
    context = {'test': 1}
    return render(request, 'test.html', context)


def demo(request):
    context = {'demo': 1}
    return render(request, 'demo.html', context)