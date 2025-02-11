# products/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'category', 
        'cost_price', 
        'selling_price',
        'manufacturer',
        'stock_quantity',
        'commission_rate',
        'created_at',
        'updated_at'
    ]
    list_filter = ['category', 'manufacturer']
    search_fields = ['name', 'manufacturer']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = [
        ('기본 정보', {
            'fields': ['name', 'category', 'manufacturer']
        }),
        ('가격 정보', {
            'fields': ['cost_price', 'selling_price', 'commission_rate']
        }),
        ('재고 정보', {
            'fields': ['stock_quantity']
        }),
    ]
    
    list_per_page = 20
