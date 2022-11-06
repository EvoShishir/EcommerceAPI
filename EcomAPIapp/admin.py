from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import (
    User,
    Category,
    Product,
    OrderItem,
    PlacedOrder,
)

UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
