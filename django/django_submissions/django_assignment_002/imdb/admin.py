from django.contrib import admin
#imdb file

from imdb.models import *

admin.site.register(Director)

admin.site.register(Actor)

admin.site.register(Movie)

admin.site.register(Rating)

admin.site.register(Cast)

# Register your models here.
