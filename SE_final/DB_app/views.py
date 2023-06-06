from django.shortcuts import render
from django.http import HttpResponse
from .models import *

import datetime

def index(request):
    return render(request, 'index.html')

def create_test_data(request):

    # 首先，我們需要確定所有的外建約束在測試資料中也一定要存在。
    # PhysicalStores 先建立一些店鋪：

    store1 = PhysicalStores.objects.create(branch_name="A店")
    store2 = PhysicalStores.objects.create(branch_name="B店")

    # Salespeople 在每個店鋪中新增銷售員：

    
    staff1 = Salespeople.objects.create(salesperson_name="小明", store_id=store1)
    staff2 = Salespeople.objects.create(salesperson_name="小王", store_id=store2)
    staff3 = Salespeople.objects.create(salesperson_name="小林", store_id=store2)
    

    # Products 建立產品：

    
    prod1 = Products.objects.create(product_model="C300", product_name="椅子A", product_price=10000, product_cost=7000, product_warranty=True)
    prod2 = Products.objects.create(product_model="C428", product_name="椅子B", product_price=15000, product_cost=9000, product_warranty=False)
    

    # Customers：

    
    #user1
    user1 = User.objects.create_user(
        username="user1",
        password="testpassword"
    )
    cust1 = Customers.objects.create(
        username=user1,
        customer_name="王大明",
        customer_gender="1",
        phone_number="0912345678",
        salesperson=staff1
    )

    #user2
    user2 = User.objects.create_user(
        username="user2",
        password="testpassword"
    )
    cust2 = Customers.objects.create(
        username=user2,
        customer_name="陳小美",
        customer_gender="2",
        phone_number="0987654321",
        salesperson=staff3
    )
    

    # MassageChairModes 建立按摩椅模式：

    
    mode1 = MassageChairModes.objects.create(massage_chair_mode_name="模式A")
    mode2 = MassageChairModes.objects.create(massage_chair_mode_name="模式B")
    

    # MassageChairs 建立按摩椅：

    
    chair1 = MassageChairs.objects.create(store_id=store1, product_model=prod1)
    chair2 = MassageChairs.objects.create(store_id=store2, product_model=prod2)
    

    # MassageChairRecord 建立按摩椅紀錄：

    
    record1 = MassageChairRecord.objects.create(customer=cust1, massage_chair=chair1, massage_chair_mode=mode1, payment="1")
    record2 = MassageChairRecord.objects.create(customer=cust2, massage_chair=chair2, massage_chair_mode=mode2, payment="2")
    

    # OnlineStoreVisits 建立線上商店參觀紀錄：

    
    visit1 = OnlineStoreVisits.objects.create(customer=cust1, product=prod1)
    visit2 = OnlineStoreVisits.objects.create(customer=cust2, product=prod2)
    

    # SalesRecords 建立銷售紀錄：

    
    sales1 = SalesRecords.objects.create(customer=cust1, product=prod1, sales_type="2", salesperson=staff1, store=store1, sales_price=10000)
    sales2 = SalesRecords.objects.create(customer=cust2, product=prod2, sales_type="2", salesperson=staff3, store=store2, sales_price=15000)
    

    # ReferralCodes 建立推薦序號：

    
    referral1 = ReferralCodes.objects.create(customer=cust1, referral_code="ABC1234", uesd_referral_code="")
    

    # ExperienceQuestionnaires 建立體驗問卷：
    
    ques1 = ExperienceQuestionnaires.objects.create(customer=cust1, usage_id=record1, willingness_to_use_again=True, massage_chair_mode_satisfaction=8)
    ques2 = ExperienceQuestionnaires.objects.create(customer=cust2, usage_id=record2, willingness_to_use_again=False, massage_chair_mode_satisfaction=6)
    

    # SalesQuestionnaires 建立銷售問卷：

    
    sales_ques1 = SalesQuestionnaires.objects.create(sales_record=sales1, sales_process_score=9, warranty_process_score=8)
    sales_ques2 = SalesQuestionnaires.objects.create(sales_record=sales2, sales_process_score=6, warranty_process_score=7)
    
    return HttpResponse("測試資料建立完成！")