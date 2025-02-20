from django.urls import path
from .views import FunFactsView, FactsDetailsView

urlpatterns = [
    path('facts/', FunFactsView.as_view(), name='fun-facts'),
    path('facts/<int:pk>/', FactsDetailsView.as_view(), name='fun-facts-details'),
]
