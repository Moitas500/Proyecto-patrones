from email.mime import image
from django.contrib import admin

from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    icon_name = 'layers'
    list_display = ['nombre', 'descripcion']
    prepopulated_fields = {'descripcion': ('nombre',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    icon_name = 'shopping_cart'
    list_display = ['nombre', 'descripcion', 'precio', 'existencia', 'disponible', 'created',
                    'updated']
    list_filter = ['disponible', 'created', 'updated']
    list_editable = ['precio', 'existencia', 'disponible']
    prepopulated_fields = {'descripcion': ('nombre',)}


admin.site.register(Product, ProductAdmin)
