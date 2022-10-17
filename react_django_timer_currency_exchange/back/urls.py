from django.urls import path
from .views import *

urlpatterns = [
    path('back/', index, name='index'),
]