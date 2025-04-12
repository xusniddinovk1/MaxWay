from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    cost = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    objects = None
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Order(models.Model):
    objects = None
    payment = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    objects = None
    count = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
