from django.urls import path
from .views import quotes_list, add,  edit_quote, delete_quote

urlpatterns = [
    path('list/', quotes_list, name='quotes_list'),
    path('edit/<id:int>/', edit_quote, name='edit_quote'),
    path('delete/<id:int>/', delete_quote, name='delete_quote'),
    path('add/', add, name='add'),
]

# the name attribute 
# can be used in html template
# {% url 'quotes_list' %}
