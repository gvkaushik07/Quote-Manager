from django.urls import path
from .views import quote_list, add_quote, edit_quote, delete_quote

urlpatterns = [
    path('', quote_list, name='quote_list'),
    path('add/', add_quote, name='add_quote'),
    path('edit/<int:pk>/', edit_quote, name='edit_quote'),
    path('delete/<int:pk>/', delete_quote, name='delete_quote'),
]