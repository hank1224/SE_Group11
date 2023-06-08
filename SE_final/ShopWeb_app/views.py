from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm 
from django.utils import timezone
from django.http import HttpResponse

from DB_app.models import *
from ShopWeb_app.forms import *

import datetime
# Create your views here.
def index(request): 
    products = Products.objects.all() 
    return render(request, 'index.html', {'products': products})

@login_required
def buy_product(request, product_id):
    buying = Products.objects.get(product_id=product_id)
    price = buying.product_price
    SalesRecords.objects.create(customer=request.user.customers, product=buying, sales_type='1', sales_price=price)
    return redirect('index')
    
def login_view(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user) 
            messages.success(request, f"Welcome back, {user.username}!") 
            return redirect('index') 
    else:
        form = AuthenticationForm() 
    return render(request, 'login.html', {'form': form}) 

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
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('index')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})
