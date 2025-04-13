from django.contrib import admin
from food.models import Category, Order, OrderProduct, Customer, Product

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Customer)
admin.site.register(Product)
