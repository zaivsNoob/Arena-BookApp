from django.urls import path
from .views import book_list, add_book

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('books/add/', add_book, name='add-book'),
]