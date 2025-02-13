from django.urls import path
from students import views

urlpatterns = [
    path('add/', views.add_name),
    path('get/', views.get_names),
]
