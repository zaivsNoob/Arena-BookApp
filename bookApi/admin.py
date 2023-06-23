from django.contrib import admin
from .models import *
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  # Display these fields in the table
    search_fields = ('title', 'author')  # Enable search functionality
    list_filter = ('author',)  # Add a filter sidebar for the 'author' field




class CartItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity')  # Display these fields in the table
    list_select_related = ('book',)  # Optimize database queries by selecting related 'book' objects

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Book, BookAdmin)