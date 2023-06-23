from django.urls import path
from .views import book_list ,cart_all

urlpatterns = [
    path('books/', book_list, name='book-list'),
       path('cart/',cart_all , name='add-to-cart'),
 
]