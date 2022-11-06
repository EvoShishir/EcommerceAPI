from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import (
    User,
    Category,
    Product,
    OrderItem,
    PlacedOrder,
)


class CustomUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "phone",
            "is_staff",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title")
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "category",
            "price",
            "image",
            "in_stock",
            "date_created",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    price = serializers.ReadOnlyField(source="product.price")
    image = serializers.ImageField(source="product.image")

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "product_name",
            "price",
            "image",
            "quantity",
        )


class PlacedOrderSerializer(serializers.ModelSerializer):
    ordered_by = serializers.ReadOnlyField(source="ordered_by.email")

    class Meta:
        model = PlacedOrder
        fields = (
            "id",
            "created_at",
            "ordered_by",
            "first_name",
            "last_name",
            "phone",
            "address",
            "zipcode",
            "items",
            "total_price",
        )


class AllOrderSerializer(serializers.ModelSerializer):
    ordered_by = serializers.ReadOnlyField(source="ordered_by.email")
    items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = PlacedOrder
        fields = (
            "id",
            "created_at",
            "ordered_by",
            "first_name",
            "last_name",
            "phone",
            "address",
            "zipcode",
            "items",
            "total_price",
        )


class UserOrderSerializer(serializers.ModelSerializer):
    ordered_by = serializers.ReadOnlyField(source="ordered_by.email")
    items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = PlacedOrder
        fields = (
            "id",
            "created_at",
            "ordered_by",
            "first_name",
            "last_name",
            "phone",
            "address",
            "zipcode",
            "items",
            "total_price",
        )
