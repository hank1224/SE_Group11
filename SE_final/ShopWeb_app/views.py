from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponse

from DB_app.models import *
from ShopWeb_app.forms import *

from django.contrib.auth.decorators import user_passes_test

# 登入狀態確認，並且區隔客戶與員工
def customer_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/ShopWeb/login')
        elif request.user.is_active and request.user.is_staff:
            return redirect('/SalesApp/index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def index(request): 
    products = Products.objects.all() 
    return render(request, 'ShopWeb/index.html', {'products': products})

@customer_login_required
def buy_product(request, product_id):
    buying = Products.objects.get(product_id=product_id)
    price = buying.product_price
    SalesRecords.objects.create(customer=request.user.customers, product=buying, sales_type='1', sales_price=price)
    return redirect('ShopWeb/index')

@customer_login_required
def order(request):
    records = SalesRecords.objects.filter(customer=request.user.customers)
    return render(request, 'ShopWeb/order.html', {'records': records})

@customer_login_required
def warranty(request):
    records = SalesRecords.objects.filter(customer=request.user.customers)
    return render(request, 'ShopWeb/warranty.html', {'records': records})

def login_view(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user) 
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('ShopWeb/index') 
    else:
        form = AuthenticationForm()
    return render(request, 'ShopWeb/login.html', {'form': form}) 

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer_name = form.cleaned_data['customer_name']
            customer_gender = form.cleaned_data['customer_gender']
            phone_number = form.cleaned_data['phone_number']
            Customers.objects.create(username=user, customer_name=customer_name, customer_gender=customer_gender,
                                     phone_number=phone_number)
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!您已註冊成功!")
            return redirect('ShopWeb/index')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'ShopWeb/register.html', {'form': form})