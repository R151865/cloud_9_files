
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', set_timezone, name='set_timezone'),
]
