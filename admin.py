from django.contrib import admin
from .models import Product, Add_Cart, Category, coupon, Billing


admin.site.register(Product)
admin.site.register(Add_Cart)
admin.site.register(Category)
admin.site.register(coupon)
admin.site.register(Billing)