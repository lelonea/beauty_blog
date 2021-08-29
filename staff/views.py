from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse('Staff page')


def categories(request, catid):
    return HttpResponse(f'<h1>Staff category</h1><p>{catid}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
