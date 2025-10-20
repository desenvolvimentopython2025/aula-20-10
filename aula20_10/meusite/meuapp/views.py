from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def teste(request):
    template = loader.get_template('paginateste.html')
    return HttpResponse(template.render())

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

