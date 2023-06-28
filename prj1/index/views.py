from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request: HttpResponse):
    return render(request, 'index/index.html')


def catalog(request: HttpResponse):
    return render(request, 'index/catalog.html')
