from django.urls import path
from staff.views import *

urlpatterns = [
    path('', index),
    path('categories/', categories),
]

