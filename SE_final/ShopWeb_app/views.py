from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponse

from DB_app.models import *
from ShopWeb_app.forms import *
from ShopWeb_app.models import CustomerWebViews

from django.template.loader import render_to_string
from SE_final import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

import random

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

def product_detail(request, product_id):
    product = Products.objects.get(product_id=product_id)
    try:
        if request.user.is_authenticated and not request.user.is_staff:
            CustomerWebViews.objects.create(customer=request.user.customers, product_id=product)
    except:
        print("CustomerWebViews error, record failed.")
    return render(request, 'ShopWeb/product_detail.html', {'product': product})

@customer_login_required
def buy_product(request, product_id):
    buying = Products.objects.get(product_id=product_id)
    price = buying.product_price
    SalesRecords.objects.create(customer=request.user.customers, product=buying, sales_type='1', sales_price=price)
    messages.success(request, f"{request.user.username} 已成功購買 " + buying.product_name + " !")
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
            if request.user.is_staff:
                return redirect('/SalesApp/index')
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

            # 重複機率1/899999，懶得處理
            random_referral_code = random.randint(100000, 999999) 
            # 重複機率1/899999，懶得處理

            ReferralCodes.objects.create(customer=user.customers, referral_code=random_referral_code)
            messages.success(request, f"Welcome, {user.username}!您已註冊成功!")
            return redirect('ShopWeb/index')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'ShopWeb/register.html', {'form': form})

@customer_login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomerEditProfileForm(request.POST, instance=request.user.customers)
        if form.is_valid():
            form.save()
            messages.success(request, f"{request.user}的個人資料已更新!")
            return redirect('ShopWeb/index')
    else:
        form = CustomerEditProfileForm(instance=request.user.customers)
        email = request.user.email
        uesd_referral_code = ReferralCodes.objects.get(customer=request.user.customers).used_referral_code
    return render(request, 'ShopWeb/edit_profile.html', {'form': form, 'email': email, 'uesd_referral_code': uesd_referral_code})

# 寄廣告信
def send_ad_email(request, customer_id):
    customer = Customers.objects.get(customer_id=customer_id)
    if not customer.username.email:
        return HttpResponse('此客戶無email資料')
    try:
        email_subject = '按摩椅推銷'
        email_template = 'Email/ad.html'
        from_email = settings.EMAIL_HOST_USER
        to_email = [customer.username.email]

        html_content = render_to_string(email_template, {'customer': customer.customer_name})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(email_subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()
    except:
        print("send_ad_email error, send failed.")