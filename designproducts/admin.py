from django.contrib import admin

from django.contrib import admin
from .models import Product, Category, UserComments

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class UserCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'designproduct', 'date_added', 'comment']

admin.site.register(UserComments, UserCommentsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
