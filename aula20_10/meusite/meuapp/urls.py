from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('teste/',views.teste,name='teste'),
    path('principal/',views.principal,name='principal'),
]