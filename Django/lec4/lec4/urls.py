from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from lec4.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
]

# https://docs.djangoproject.com/en/5.1/howto/static-files/#serving-static-files-during-development
urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
)

 