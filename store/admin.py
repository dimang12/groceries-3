from django.contrib import admin
from .models import Category, Product

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('cateName', 'cateDetail') 
    

admin.site.register(Category, CategoriesAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("proName","categoryId", "proPrice", "proWeight")
    list_editable = ("proPrice",)
    ordering = ("proName", "categoryId") 
    list_per_page: int = 15

admin.site.register(Product, ProductsAdmin)