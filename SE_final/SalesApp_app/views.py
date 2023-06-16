from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from DB_app.models import *
from .forms import *

from django.template.loader import render_to_string
from SE_final import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


# 登入狀態確認，並且區隔客戶與員工
def staff_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/ShopWeb/login')
        elif request.user.is_active and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def index(request):
    return render(request, 'SalesApp/index.html')

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
        print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'SalesApp/login.html', {'form': form}) 

def register(request):
    if request.method == 'POST':
        form = SalespeopleRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            salesperson_name = form.cleaned_data['salesperson_name']
            store_id = form.cleaned_data['store_id']
            Salespeople.objects.create(staff_username=user, salesperson_name=salesperson_name, store_id=store_id)
            messages.success(request, f"New account created: {user.username}")
            login(request, user)
            return redirect('/SalesApp/index')
        print(form.errors)
        return redirect('/SalesApp/register')
    else:
        form = SalespeopleRegisterForm()
        return render(request, 'SalesApp/register.html', {'form': form})

@staff_login_required
def sales_sell(request):
    if request.method == 'POST':
        form = SalesRecordsForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            sales_price = form.cleaned_data['sales_price']
            SalesRecords.objects.create(customer=customer, product=product, sales_price=sales_price, sales_type='2', salesperson=request.user.salespeople, store=request.user.salespeople.store_id)
            messages.success(request, f"Success!")
            return redirect('/SalesApp/index')
        print(form.errors)
    else:
        initial = {'sales_type': '2', 'salesperson': request.user.salespeople}  # 將預設值設定為2（sales_type）以及當前登入的使用者（salesperson）
        form = SalesRecordsForm(initial=initial)
    return render(request, 'SalesApp/sales_sell.html', {'form': form})

@staff_login_required
def actions(request):
    Customers_list = Customers.objects.filter(salesperson=request.user.salespeople)
    return render(request, 'SalesApp/actions.html', {'Customers_list': Customers_list})

# 寄廣告信
def send_ad_email(request, customer_id):
    customer = Customers.objects.get(customer_id=customer_id)
    if not customer.username.email:
        return HttpResponse('此客戶無email資料')
    try:
        email_subject = '按摩椅廣告信'
        email_template = 'Email/ad.html'
        from_email = settings.EMAIL_HOST_USER
        to_email = [customer.username.email]
        print("sending email to " + customer.username.email)
        html_content = render_to_string(email_template, {'customer': customer.customer_name, 'customer_id': customer_id})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(email_subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()
        messages.success(request, f"寄送廣告給 {customer.username} 成功!")
        return redirect('/SalesApp/actions')
    except:
        print("send_ad_email error.")
        return redirect('/SalesApp/actions')

# 寄EQ信
def send_EQ_email(request, sales_record_id):
    customer_id = SalesRecords.objects.get(sales_record_id=sales_record_id).customer.customer_id
    customer = Customers.objects.get(customer_id=customer_id)
    if not customer.username.email:
        return HttpResponse('此客戶無email資料')
    try:
        email_subject = '售後服務問券'
        email_template = 'Email/WarrantyProcessEQ.html'
        from_email = settings.EMAIL_HOST_USER
        to_email = [customer.username.email]
        print("sending email to " + customer.username.email)
        html_content = render_to_string(email_template, {'customer': customer.customer_name, 'sales_record_id': sales_record_id, 'customer_id': customer_id})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(email_subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()
        messages.success(request, f"寄送問券給 {customer.username} 成功!")
        return redirect('/SalesApp/actions')
    except:
        print("send_ad_email error.")
        return redirect('/SalesApp/actions')
    