from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Add Product to Admin Site
admin.site.register(Product, ProductAdmin)

# Add Offer to Admin Site
admin.site.register(Offer, OfferAdmin)
