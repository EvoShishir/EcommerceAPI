from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import (
    User,
    Category,
    Product,
    OrderItem,
    PlacedOrder,
)

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
