from django.contrib import admin
from .models import Review, Review_Comment
# Register your models here.

admin.site.register(Review)
admin.site.register(Review_Comment)