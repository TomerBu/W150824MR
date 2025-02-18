from django.urls import path
from .views import index, edit_student, KittenViews

urlpatterns = [
    path('students/', index, name='students'),
    path('students/<int:id>', edit_student, name='student actions'),
    path('kittens/', KittenViews.as_view(), name='kittens')
]
