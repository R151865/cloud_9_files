from django.contrib import admin

from django.urls import path, include

from .views import *

urlpatterns = [
    path('post/', create_post),
    path('post/<int:post_id>/', get_post),
    path('post/<int:post_id>/react/', react_to_post),
    path('post/<int:post_id>/delete/', delete_post),
    
    path('comment/<int:comment_id>/reply/create/', reply_to_comment),
    path('comment/<int:comment_id>/react/', react_to_comment),
    path('post/<int:post_id>/comment/create/', create_comment),

]




# curl -d 'user_id=1&content=hey anajali' http://127.0.0.1:8080/fb_post/post/
# curl -d 'user_id=1&content="hey anajali" ' http://127.0.0.1:8000/fb_post/comment/2/reply/create/
# curl -d 'user_id=1&reaction_type=HAHA' http://127.0.0.1:8000/fb_post/comment/1/react/
# curl -d 'user_id=1' http://127.0.0.1:8000/fb_post/post/1/delete/
# curl -d 'user_id=5&reaction_type=HAHA' http://127.0.0.1:8000/fb_post/post/5/react/
# curl -d 'user_id=3' http://127.0.0.1:8000/fb_post/post/6/comment/create/


#curl -H '{"user_id"=4,"content"="HII"}' "Authorization: Bearer StIJnckt05q39A4YTlzKFVzkCGqp0j"    http://127.0.0.1:8080/fb_post/post/


#curl -H "Content-type:application/json" -d '{"user_id":4,"content":"HII"}' -H "Authorization: Bearer StIJnckt05q39A4YTlzKFVzkCGqp0j" http://127.0.0.1:8080/fb_post/post/