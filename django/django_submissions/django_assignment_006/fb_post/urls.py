from django.urls import path, include
from .views import *
urlpatterns = [
    path('<int:post_id>/', set_timezone, name='set_timezone'),
]
