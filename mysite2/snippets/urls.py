from django.urls import path
from .views import *


urlpatterns = [
    path('dummy/', dummy_view),

]
#curl -d ' ' "http://127.0.0.1:8000/snippets/dummy/"
#curl -d 'title=sulthan' "http://127.0.0.1:8000/snippets/dummy/"