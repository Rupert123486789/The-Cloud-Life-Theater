from django.contrib import admin
from .models import Movie, Movie_Comment

# Register your models here.

admin.site.register(Movie)
admin.site.register(Movie_Comment)