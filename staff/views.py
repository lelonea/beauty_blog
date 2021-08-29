from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Staff page')


def categories(request):
    return HttpResponse('Staff category')
