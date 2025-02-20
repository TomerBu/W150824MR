from django.urls import path
from .views import FunFactsView

urlpatterns = [
    path('facts/', FunFactsView.as_view(), name='fun-facts'),
]
