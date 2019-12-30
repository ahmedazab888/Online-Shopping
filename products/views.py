from django.http import HttpResponse
from django.shortcuts import render


# Mapping products => index
def index(request):
    return HttpResponse('HelloWorld!')


def new(request):
    return HttpResponse('New Products')
