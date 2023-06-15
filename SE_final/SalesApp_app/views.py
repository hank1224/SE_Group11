from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from DB_app.models import *

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
            return redirect('/SalesApp/index')
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
    else:
        form = AuthenticationForm()
    return render(request, 'SalesApp/login.html', {'form': form}) 

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
        print("send_ad_email error.")