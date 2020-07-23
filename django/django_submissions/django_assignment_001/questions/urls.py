from django.urls import path

from . import views

urlpatterns = [
    #questions/
    path('',views.get_list_of_questions,name='get_list_of_questions'),
    #question/create/
    path('create/',views.create_question,name='create_question'),
   #question/3/get/
    path('<int:question_id>/get/',views.get_question,name='get_question'),
    #question/4/update/
    path('<int:question_id>/update/',views.update_question,name='update_question'),
    #question/5/delete/
    path('<int:question_id>/delete/',views.delete_question,name='delete_question'),


]
