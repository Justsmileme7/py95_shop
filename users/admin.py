from django.contrib import admin
from catalog.models import (Category, Product, Seller, Discount, Order, Cashback, Promocode, ProductImage)

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'price')
    search_fields = ('article', 'name', 'price')



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(Cashback)
admin.site.register(Promocode)
admin.site.register(ProductImage)

