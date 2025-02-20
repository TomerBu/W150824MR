from django.urls import path, include
from .views import PostsView2, PostActions2, APIMap, DemoViewSet, CommentsViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('demos', DemoViewSet, basename='demo')
router.register('comments', CommentsViewSet, basename='comment')

urlpatterns = [
    path('router/', include(router.urls)),
    path('', APIMap.as_view(), name='map'),   
    path('posts/', PostsView2.as_view(), name='posts'),   
    path('posts/<int:pk>', PostActions2.as_view(), name='post-actions'),   
]
