from django.contrib import admin
from .models import Category, Product, xyz

# Register your models here.

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(xyz)

# class categoryAdmin(admin.ModelAdmin):
#     list_display = ['CategoryName', 'priceOfProduct', 'rating']
#     list_filter = ['CategoryName', 'priceOfProduct', 'rating']
# admin.site.register(categoryAdmin)

# class productadmin(admin.ModelAdmin):
#     list_display = ['CategoryName']
# admin.site.register(productadmin)
