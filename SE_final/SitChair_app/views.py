from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import *
from DB_app.models import PhysicalStores, ExperienceReservations, Salespeople

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
            form.instance.customer = request.user.customers
            form.save()
        messages.success(request, f"{request.user}已開始按摩服務!")
        return redirect('SitChair/use_massage_chair')
    else:
        form = MassageChairRecordForm()
        return render(request, 'SitChair/use_massage_chair.html', {'form': form})
    
@customer_login_required
def list_massage_chair_record(request):
    massage_record = MassageChairRecord.objects.filter(customer=request.user.customers).order_by('-start_time')
    return render(request, 'SitChair/list_massage_chair_record.html', {'massage_record': massage_record})
    
@customer_login_required
def experience_questionnaire(request, usage_id):
    if request.method == 'POST':
        form = ExperienceQuestionnaireForm(data=request.POST)
        if form.is_valid():
            form.instance.usage_id = MassageChairRecord.objects.get(usage_id=usage_id)
            form.instance.customer = request.user.customers
            form.save()
            MassageChairRecord.objects.filter(usage_id=usage_id).update(experience_questionnaires_fill=True)
        messages.success(request, f"紀錄編號{ usage_id }，體驗問券填寫成功!")
        return redirect('SitChair/list_massage_chair_record')
    else:
        form = ExperienceQuestionnaireForm()
        return render(request, 'SitChair/experience_questionnaire.html', {'form': form, 'usage_id': usage_id})
    
@customer_login_required
def experience_reservation(request):
    if request.method == 'POST':
        form = ExperienceReservationForm(data=request.POST)
        if form.is_valid():
            form.instance.customer = request.user.customers
            form_store = form.cleaned_data['store_id']
            try:
                chose_salespeople = random.choice(Salespeople.objects.filter(store_id=form_store))
                form.instance.salespeople = chose_salespeople
            except:
                form.instance.salespeople = Salespeople.objects.get(salespeople_id=1)
                print("None salespeople chose, default salespeople_id=1")
            form.save()
        messages.success(request, f"體驗預約成功!")
        return redirect('SitChair/experience_reservation')
    else:
        form = ExperienceReservationForm()
        stores = PhysicalStores.objects.all()
        reservations = ExperienceReservations.objects.filter(customer=request.user.customers).order_by('-reservation_time')
        return render(request, 'SitChair/experience_reservation.html', {'form': form, 'stores': stores, 'reservations': reservations})

