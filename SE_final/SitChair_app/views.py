from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import *

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

def login_view(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user) 
            messages.success(request, f"Welcome back, {user.username}!")
            if request.user.is_staff:
                return redirect('/SalesApp/index')
            return redirect('SitChair/index') 
    else:
        form = AuthenticationForm()
    return render(request, 'SitChair/login.html', {'form': form}) 

def index(request):
    return render(request, 'SitChair/index.html')

@customer_login_required
def use_massage_chair(request):
    if request.method == 'POST':
        form = MassageChairRecordForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.instance.customer = request.user.customers
            form.save()
        messages.success(request, f"{request.user}已開始按摩服務!")
        return redirect('SitChair/use_massage_chair')
    else:
        form = MassageChairRecordForm()
        return render(request, 'SitChair/use_massage_chair.html', {'form': form})

