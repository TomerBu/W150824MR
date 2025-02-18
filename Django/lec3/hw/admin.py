from django.contrib import admin

# Register your models here.

from .models import Post, Author, Category, Comment

admin.site.register([Post, Author, Category, Comment])

# python manage.py createsuperuser