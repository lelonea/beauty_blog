from django.urls import path
from staff.views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:catid>/', categories, name='catid'),
]


