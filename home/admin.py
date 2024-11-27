from django.contrib import admin
from home.models import Contact
from .models import Product, CartItem

# Register your models here.
admin.site.register(Contact)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "stock", "img_url"]


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "added_at"]
