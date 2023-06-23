from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import *
from .serializers import *

# Create your views here.
@api_view(['GET','POST'])
def book_list(request):
    if request.method=="GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)        

@api_view(['GET','POST'])
def cart_all(request):
    if request.method=="GET":
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)