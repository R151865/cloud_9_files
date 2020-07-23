from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
    path('app1/', include('app1.urls')),

]