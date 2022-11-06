from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import login

from rest_framework import generics, permissions, status, authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .models import (
    User,
    Category,
    Product,
    OrderItem,
    PlacedOrder,
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    OrderItemSerializer,
    PlacedOrderSerializer,
    AllOrderSerializer,
    UserOrderSerializer,
)


@api_view(["GET"])
def getRoutes(request):

    routes = [
        {"Go to '/swagger' and get information about the corresponding route if you are confused about the data that is needed to be sent."},

        {"user: 'All categories' /categories; Method: GET"},
        {"user: 'Single Category' /categories/{{<id>}}; Method: GET"},
        {"admin: 'Create Category' /create-category; Method: POST"},
        {"admin: 'Update or Delete' /edit-category/{{<id>}}; Method: PUT/DELETE"},
        {"user: 'All products' /products; Method: GET"},
        {"user: 'Single product' /products/{{<id>}}; Method: GET"},
        {"admin: 'Create Product' /create-product; Method: POST"},
        {"admin: 'Update or Delete' /edit-product/{{<id>}}; Method: PUT/DELETE"},
        {"user: 'User registration' /auth/users"},
        {"user: 'User login' /auth/jwt/create"},
        {"user: 'View or Edit user profile' /auth/users/me; Method: GET/PUT"},
        {"user: 'Reset Password Request' /auth/users/reset_password; Method: POST"},
        {
            "user: 'Reset Password Confirm' /auth/users/reset_password_confirm; Method: POST"
        },
        {"user: 'User Email Verification' /auth/users/activation; Method: POST"},
        {"admin: 'Get All Users' /auth/users; Method: GET"},
        {"admin: 'Get single User' /auth/users/{{<id>}}; Method: GET"},
        {"user: 'Create Order Item' /create-order-item; Method: POST"},
        {"user: 'Get Order Items' /get-order-item; Method: GET"},
        {"user: 'Update or Delete Order Items' /get-order-item; Method: PUT/DELETE"},
        {"user: 'Get User Orders' /my-orders; Method: GET"},
        {"user: 'Place an Order' /create-order; Method: POST"},
        {"admin: 'Get All Orders' /all-orders; Method: GET"},
        {"admin: 'Get or Delete an Order' /all-orders/{{<id>}}; Method: GET/DELETE"},
    ]
    return Response(routes)


class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategory(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EditCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProduct(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EditProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateOrder(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PlacedOrder.objects.all()
    serializer_class = PlacedOrderSerializer

    def perform_create(self, serializer):
        serializer.save(ordered_by=self.request.user)


class ListUserOrders(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        ordered_by = PlacedOrder.objects.filter(ordered_by=request.user)
        serializer = UserOrderSerializer(ordered_by, many=True)
        return Response(serializer.data)


class GetAllOrders(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = PlacedOrder.objects.all()
    serializer_class = AllOrderSerializer


class GetOrDeleteOrders(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = PlacedOrder.objects.all()
    serializer_class = AllOrderSerializer


class CreateOrderItem(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GetOrderItem(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        owner = OrderItem.objects.filter(owner=request.user)
        serializer = OrderItemSerializer(owner, many=True)
        return Response(serializer.data)


class EditOrderItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
