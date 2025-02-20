from django.contrib import admin

from blog.models import UserProfile, Post, Comment ,PostUserLikes
 
admin.site.register([UserProfile, Post, Comment, PostUserLikes])