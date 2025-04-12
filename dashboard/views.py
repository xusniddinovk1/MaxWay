from django.contrib.gis.db.backends.oracle.schema import OracleGISSchemaEditor
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from food.models import *
from . import services
from . import forms


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
        return render(request, "dashboard/login.html")


def logout_page(request):
    logout(request)
    return redirect("login_page")


def main_dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    customer = Customer.objects.all()
    orders = Order.objects.all()
    categories_product = []
    table_list = services.get_table()
    print(table_list)
    for category in categories: