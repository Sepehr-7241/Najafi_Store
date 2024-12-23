from django.contrib import admin
from .models import Category, Product, FooterProductCategory, LikeProduct

admin.site.register(Category)
admin.site.register(FooterProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_delete', 'price']
    list_editable = ['is_active', 'is_delete', 'price']
    raw_id_fields = ['category']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(LikeProduct)
class LikeProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']
