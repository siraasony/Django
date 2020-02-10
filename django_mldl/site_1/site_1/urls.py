from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #127.0.0.1:8000
    #path('',),
    path('', views.index),
    path('hello/', views.hello, name='hello_main')
]
