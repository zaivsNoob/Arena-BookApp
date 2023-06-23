from rest_framework import serializers
from .models import Book,CartItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'