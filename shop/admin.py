from django.contrib import admin

from shop.models import Product, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('vendor_code',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
