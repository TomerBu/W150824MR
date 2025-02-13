from django.urls import path
from students import views

urlpatterns = [
    path('add/', views.add_html),
    path('get/', views.get_html),
    path('edit/<int:id>', views.edit_html),
    path('get_db/', views.view_list_db),
]
