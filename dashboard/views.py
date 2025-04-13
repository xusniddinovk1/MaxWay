from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . import services
from .forms import *


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
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


@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
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


@login_required_decorator
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


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')


@login_required_decorator
def product_list(request):
    products = Product.objects.all()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')


def user_list(request):
    users = Customer.objects.all()
    ctx = {
        "users": users
    }
    return render(request, 'dashboard/user/list.html', ctx)


@login_required_decorator
def user_create(request):
    model = Customer()
    form = UserForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/user/form.html', ctx)


def user_edit(request, pk):
    model = Customer.objects.get(pk=pk)
    form = forms.UserForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('user_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_delete(request, pk):
    model = Customer.objects.get(pk=pk)
    model.delete()
    return redirect("category_list")


@login_required_decorator
def order_list(request):
    orders = Order.objects.all()
    ctx = {
        'orders': orders
    }
    return render(request, "dashboard/order/list.html", ctx)


@login_required_decorator
def customer_order_list(request, id):
    customer_orders = services.get_order_by_user(id=id)
    ctx = {
        'customer_orders': customer_orders
    }
    return render(request, "dashboard/customer_order/list.html", ctx)


@login_required_decorator
def order_product_list(request, id):
    order_products = services.get_product_by_order(id=id)
    ctx = {
        'order_product': order_products
    }
    return render(request, "dashboard/order_product/list.html", ctx)
