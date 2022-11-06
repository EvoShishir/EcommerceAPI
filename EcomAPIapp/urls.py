from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    getRoutes,
    ListCategory,
    DetailCategory,
    ListProduct,
    DetailProduct,
    CreateCategory,
    EditCategory,
    CreateProduct,
    EditProduct,
    ListUserOrders,
    CreateOrder,
    GetAllOrders,
    GetOrDeleteOrders,
    CreateOrderItem,
    GetOrderItem,
    EditOrderItem,
)

urlpatterns = [
    path("", getRoutes),
    path("categories/", ListCategory.as_view(), name="Categories"),
    path("categories/<int:pk>", DetailCategory.as_view(), name="SingleCategory"),
    path("create-category/", CreateCategory.as_view(), name="CreateCategory"),
    path("edit-category/<str:pk>", EditCategory.as_view(), name="EditCategory"),
    path("products/", ListProduct.as_view(), name="Products"),
    path("products/<int:pk>", DetailProduct.as_view(), name="SingleProduct"),
    path("create-product/", CreateProduct.as_view(), name="CreateProduct"),
    path("edit-product/<int:pk>", EditProduct.as_view(), name="EditProduct"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("create-order-item/", CreateOrderItem.as_view(), name="CreateOrderItem"),
    path("get-order-items/", GetOrderItem.as_view(), name="GetOrderItems"),
    path("edit-order-items/<str:pk>", EditOrderItem.as_view(), name="EditOrderItem"),
    path("create-order/", CreateOrder.as_view(), name="CreateOrder"),
    path("my-orders/", ListUserOrders.as_view(), name="ListOrders"),
    path("all-orders/", GetAllOrders.as_view(), name="GetAllOrders"),
    path("all-orders/<str:pk>", GetOrDeleteOrders.as_view(), name="GetOrDeleteOrders"),
]
