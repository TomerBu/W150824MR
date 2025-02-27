from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from lec4.settings import MEDIA_ROOT, MEDIA_URL
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# https://docs.djangoproject.com/en/5.1/howto/static-files/#serving-static-files-during-development
urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
)