# from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('contact_us',views.contact_us, name='contact-us'),
    url('register', views.register, name='register'),
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout'),

    url('test', views.test, name='test'),
]
