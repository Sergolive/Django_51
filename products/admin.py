from django.contrib import admin

from .models import CategoryModel, ProductsModel, CartModel

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']

@admin.register(ProductsModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title', 'price']
    list_display = ['id', 'title', 'price', 'count', 'updated_at', 'created_at']
    list_filter = ['created_at']

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'product', 'total_price']
    list_display = ['id', 'product', 'total_price', 'total_count']


# Register your models here.

