from django.urls import path, include
from .views import CommentsViewSet, PostsViewSet, UserProfileViewSet, LikesViewSet
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import UsersViewSet
router.register('auth', UsersViewSet, basename='auth')

router.register('comments', CommentsViewSet, basename='comment')
router.register('posts', PostsViewSet, basename='posts')
router.register('user-profile', UserProfileViewSet, basename='user-profile')
router.register('likes', LikesViewSet, basename='likes')



from rest_framework.authtoken import views as auth_views
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('login/', auth_views.obtain_auth_token)
]
