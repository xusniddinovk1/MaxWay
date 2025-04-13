from django.contrib.gis.db.backends.oracle.schema import OracleGISSchemaEditor
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from food.models import *
from . import services
from forms import *


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
    customers = Customer.objects.all()
    orders = Order.objects.all()
    categories_product = []
    table_list = services.get_table()
    print(table_list)
    for category in categories:
        categories_product.append(
            {
                "category": category.name,
                "product": len(Product.objects.filter(categoty_id=category.id))
            }
        )

        ctx = {
            "counts":
                {
                    "categories": len(categories),
                    "products": len(products),
                    "customers": len(customers),
                    "orders": len(orders),
                },
            "category_product": categories_product,
            "table_list": table_list
        }

        return render(request, 'dashboard/index.html', ctx)


def category_list(request):
    categories = Category.objects.all()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_delete(request):
    model = Category()
    model.delete()
    return redirect('category_list')
