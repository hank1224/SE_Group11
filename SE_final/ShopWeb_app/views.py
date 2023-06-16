from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponse

from DB_app.models import *
from ShopWeb_app.forms import *

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
            CustomerWebViews.objects.create(customer=request.user.customers, product=product)
    except:
        print("CustomerWebViews error, record failed.")
    return render(request, 'ShopWeb/product_detail.html', {'product': product})

@customer_login_required
def buy_product(request, product_id):
    buying = Products.objects.get(product_id=product_id)
    price = buying.product_price
    print(request.user.customers.salesperson)
    SalesRecords.objects.create(customer=request.user.customers, product=buying, sales_type='1', sales_price=price, salesperson=request.user.customers.salesperson)
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
            try:
                all_salespeople = Salespeople.objects.all()
                random_salesperson = random.choice(all_salespeople)
            except:
                random_salesperson = Salespeople.objects.get(salesperson_id=1)
                print("register random salesperson error, used default.")
            Customers.objects.create(username=user, customer_name=customer_name, customer_gender=customer_gender, phone_number=phone_number, salesperson=random_salesperson)
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
        used_referral_code = ReferralCodes.objects.get(customer=request.user.customers).used_referral_code
        salesperson = request.user.customers.salesperson
    return render(request, 'ShopWeb/edit_profile.html', {'form': form, 'email': email, 'used_referral_code': used_referral_code, 'salesperson': salesperson})

@customer_login_required
def referral_code(request):
    referral_code_instance = ReferralCodes.objects.get(customer=request.user.customers)
    if request.method == 'POST':
        form = ReferralCodeForm(request.POST, instance=referral_code_instance)
        if form.is_valid():
            check_referral_code = form.cleaned_data['used_referral_code']
            if ReferralCodes.objects.filter(referral_code=check_referral_code).exists():
                if check_referral_code == referral_code_instance.referral_code:
                    messages.error(request, f"無法填寫自己作爲推薦人")
                    return redirect('ShopWeb/index')
                form.save()
                messages.success(request, f"{request.user}成功填寫推薦碼!")
                return redirect('ShopWeb/index')
            else:
                messages.error(request, '此推薦碼不存在')
                return redirect('ShopWeb/index')
    else:
        if referral_code_instance.used_referral_code:
            form = ReferralCodeForm_unfillable(instance=referral_code_instance)
        else:
            form = ReferralCodeForm(instance=referral_code_instance)
        return render(request, 'ShopWeb/referral_code.html', {'form': form, 'referral_code_instance': referral_code_instance})

#有夠蠢，乾脆用傳統form
@customer_login_required
def sales_process_EQ(request, sales_record_id):
    sales_record = SalesRecords.objects.get(sales_record_id=sales_record_id)
    if request.method == 'POST':
        form = SalesProcessEQForm(request.POST)
        print(form.data)
        if form.is_valid():
            SalesQuestionnaires.objects.get_or_create(sales_record=sales_record, **form.cleaned_data)
            SalesQuestionnaires.objects.filter(sales_record=sales_record).update(sales_process_score=form.data['sales_process_score'])
            messages.success(request, f"{request.user}已成功填寫EQ!")
            return redirect('ShopWeb/index')
    else:
        form = SalesProcessEQForm(instance=sales_record)
        return render(request, 'ShopWeb/sales_process_EQ.html', {'form': form, 'sales_record': sales_record})

#沒優化 
def warranty_process_EQ(request, sales_record_id):
    if not SalesQuestionnaires.objects.filter(sales_record=sales_record_id).exists():
        SalesQuestionnaires.objects.create(sales_record=SalesRecords.objects.get(sales_record_id=sales_record_id))

    if SalesQuestionnaires.objects.get(sales_record=sales_record_id).warranty_process_score:
        return HttpResponse("<h1>您已填過此表單</h1>")
    else:
        sales_record = SalesRecords.objects.get(sales_record_id=sales_record_id)
        if request.method == 'POST':
            form = WarrantyProcessEQForm(request.POST)
            print(form.data)
            if form.is_valid():
                SalesQuestionnaires.objects.filter(sales_record=sales_record).update(warranty_process_score=form.data['warranty_process_score'])
                messages.success(request, "您已成功填寫EQ!")
                return redirect('ShopWeb/index')
            print(form.errors)
        else:
            form = WarrantyProcessEQForm(instance=sales_record)
            return render(request, 'ShopWeb/warranty_process_EQ.html', {'form': form, 'sales_record_id': sales_record.sales_record_id, 'customer_id': sales_record.customer.customer_id})

def customer_ad_click(request, customer_id):
    try:
        CustomerADClicks.objects.create(customer_id=customer_id)
    except:
        print("customer_ad_click error, not created")
    return redirect('ShopWeb/index')