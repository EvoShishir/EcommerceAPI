from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["username", "phone", "first_name", "last_name"]
    USERNAME_FIELD = "email"

    def get_username(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default="default.png")
    in_stock = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)


class PlacedOrder(models.Model):
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    items = models.ManyToManyField(OrderItem)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.ordered_by}"
