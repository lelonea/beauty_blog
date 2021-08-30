from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = ['Login', 'Categories', 'About', 'Contacts']


def index(request):
    posts = Staff.objects.all()
    return render(request, 'staff/home.html', {'posts': posts, 'title': 'Staff page', 'menu': menu})


def categories(request, catid):
    return HttpResponse(f'<h1>Staff category</h1><p>{catid}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
