from django.urls import path, include
from .views import CommentsViewSet, PostsViewSet, UserProfileViewSet, LikesViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('comments', CommentsViewSet, basename='comment')
router.register('posts', PostsViewSet, basename='posts')
router.register('user-profile', UserProfileViewSet, basename='user-profile')
router.register('likes', LikesViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
