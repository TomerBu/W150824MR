from django.urls import path
from .views import PostsView2, PostActions2, APIMap

urlpatterns = [
    path('', APIMap.as_view(), name='map'),   
    path('posts/', PostsView2.as_view(), name='posts'),   
    path('posts/<int:pk>', PostActions2.as_view(), name='post-actions'),   
]
