from django.contrib import admin
from .models import Cart, CartDetail, Order, OrderDetail

admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)
