from django.contrib import admin

# Register your models here.
from .models import Category, Product, Slider, ProductReview

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock',
'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
admin.site.register(Slider)
admin.site.register(ProductReview)