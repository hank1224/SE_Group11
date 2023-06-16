from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from django.contrib.auth.models import User
from .models import *
import datetime
import random


def gateway(request):
    login_state = "尚未登入"
    if not request.user.is_staff and request.user.is_authenticated:
        login_state = str(request.user.username) + "，客戶"
    elif request.user.is_superuser:
        login_state = str(request.user.username) + "，後台管理員"
    elif request.user.is_staff and request.user.is_authenticated:
        login_state = str(request.user.username) + "，員工"
        
    return render(request, 'gateway.html', {'login_state': login_state})

def create_test_data(request):

    # 檢查是否已建立過測試資料
    if len(PhysicalStores.objects.all()) > 0:
        return HttpResponse("已建立過測試資料，若前面創建出錯請刪資料庫重來！")

    # 首先，我們需要確定所有的外建約束在測試資料中也一定要存在。
    # PhysicalStores 先建立一些店鋪：
    store1 = PhysicalStores.objects.create(branch_name="實體店A")
    store2 = PhysicalStores.objects.create(branch_name="實體店B")
    store3 = PhysicalStores.objects.create(branch_name="實體店C")
    store4 = PhysicalStores.objects.create(branch_name="實體店D")
    store5 = PhysicalStores.objects.create(branch_name="實體店E")

    # Salespeople 建立銷售員：
    for i in range(1, 6):
        username = "staff" + str(i)
        password = "0000"
        is_staff = True

        user = User.objects.create_user(username=username, password=password, is_staff=is_staff)

        salesperson_name = "銷售員" + str(i)
        store = PhysicalStores.objects.get(store_id=i)
        staff_username = User.objects.get(username=username)

        salesperson = Salespeople.objects.create(salesperson_name=salesperson_name, store_id=store, staff_username=staff_username)

    # Products 建立產品：
    prod1 = Products.objects.create(product_model="HY-3068A", product_name="WULA超有力小沙發按摩椅", product_price=25000, product_cost=20000, product_warranty=False)
    prod2 = Products.objects.create(product_model="HY-5083", product_name="追夢椅PLUS(石墨烯升級款)", product_price=72000, product_cost=50000, product_warranty=True)
    prod3 = Products.objects.create(product_model="HY-5082A", product_name="V-Motion一健椅", product_price=108000, product_cost=80000, product_warranty=True)
    prod4 = Products.objects.create(product_model="HY-5013", product_name="商務艙PLUS零重力按摩椅", product_price=39000, product_cost=30000, product_warranty=False)
    prod5 = Products.objects.create(product_model="HY-CR52-GY", product_name="樂享起身沙發椅 (多功能電動沙發/起身椅)", product_price=15000, product_cost=10000, product_warranty=False)    

    # Customers：
    salespeople = Salespeople.objects.all()

    for i in range(1,9):
        # create user
        username = "user" + str(i)
        password = "0000"
        email = str(random.randint(1000,9999)) + "@gmail.com"
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        # create customer
        customer_name = "顧客" + str(i)
        customer_gender = str(i % 4 + 1)  # 1~4循環
        phone_number = "0912345678"
        salesperson =  salespeople[i % len(salespeople)]
        customer = Customers.objects.create(
            username=user,
            customer_name=customer_name,
            customer_gender=customer_gender,
            phone_number=phone_number,
            salesperson=salesperson
        )
    
    # MassageChairModes 建立按摩椅模式：  
    mode1 = MassageChairModes.objects.create(massage_chair_mode_name="模式A")
    mode2 = MassageChairModes.objects.create(massage_chair_mode_name="模式B")
    mode3 = MassageChairModes.objects.create(massage_chair_mode_name="模式C")
    mode4 = MassageChairModes.objects.create(massage_chair_mode_name="模式D")
    mode5 = MassageChairModes.objects.create(massage_chair_mode_name="模式E")

    # MassageChairs 建立公共按摩椅：
    chair1 = MassageChairs.objects.create(store_id=store1, product_model=prod1)
    chair2 = MassageChairs.objects.create(store_id=store2, product_model=prod2)
    chair3 = MassageChairs.objects.create(store_id=store3, product_model=prod3)
    chair4 = MassageChairs.objects.create(store_id=store4, product_model=prod4)
    chair5 = MassageChairs.objects.create(store_id=store5, product_model=prod5)
    

    # MassageChairRecord 建立按摩椅紀錄：
    customers = Customers.objects.all()
    massage_chairs = [chair1, chair2, chair3, chair4, chair5]
    modes = [mode1, mode2, mode3, mode4, mode5]
    payments = ['1', '2']

    # 建立25筆按摩椅紀錄
    for i in range(50):
        customer = random.choice(customers)
        massage_chair = random.choice(massage_chairs)
        massage_chair_mode = random.choice(modes)
        payment = random.choice(payments)
        
        record = MassageChairRecord.objects.create(customer=customer, massage_chair=massage_chair, 
                                                massage_chair_mode=massage_chair_mode, payment=payment)
        record.save()
    

    # CustomerWebViews 建立線上商店參觀紀錄：
    for i in range(50):
        cust = random.choice(customers)
        prod = random.choice([prod1, prod2, prod3, prod4, prod5])
        visit = CustomerWebViews.objects.create(customer=cust, product=prod)
    

    # SalesRecords 建立銷售紀錄：
    for i in range(100):
        cust = random.choice(customers)
        prod = random.choice([prod1, prod2, prod3, prod4, prod5])
        sales_type = random.choice(["1", "2"])
        if sales_type == "1":
            store = None
            sales_price = Products.objects.get(product_id=prod.product_id).product_price
        else:
            store = random.choice([store1, store2, store3])
        salesperson = random.choice(salespeople)
        orgin_price = Products.objects.get(product_id=prod.product_id).product_price
        addion = random.randint(1, 30)*100
        sales_price = orgin_price + addion
        SalesRecords.objects.create(customer=cust, product=prod, sales_type=sales_type, salesperson=salesperson, store=store, sales_price=sales_price)

    # ReferralCodes 建立推薦序號：
    for customer in customers:
        ReferralCodes.objects.create(customer=customer, referral_code=str(random.randint(100000,999999)), used_referral_code="")
    chose_referral_codes = random.choice(ReferralCodes.objects.all()).referral_code
    for i in range(3):
        referral_code = random.choice(ReferralCodes.objects.all())
        referral_code.used_referral_code = chose_referral_codes
        referral_code.save()


    
    # ExperienceQuestionnaires 建立體驗問卷：
    massage_chair_records = MassageChairRecord.objects.all()
    for record in massage_chair_records:
        ran_num = random.randint(1, 10)
        ran_TF = random.choice([True, False])
        ExperienceQuestionnaires.objects.create(customer=record.customer, usage_id=record, willingness_to_use_again=ran_TF, massage_chair_mode_satisfaction=ran_num)

    # SalesQuestionnaires 建立銷售問卷：
    sales_records = SalesRecords.objects.all()
    for record in sales_records:
        ran_num = random.randint(1, 10)
        SalesQuestionnaires.objects.create(sales_record=record, sales_process_score=ran_num, warranty_process_score=ran_num)

    # ExperienceReservations 建立體驗預約：
    customers = Customers.objects.all()
    stores = PhysicalStores.objects.all()
    now = datetime.datetime.now()
    for i in range(2):
        for customer in customers:
            hour = random.randint(0, 99)
            minute = random.randrange(0, 4) * 15
            seconds = 0
            time_delta = datetime.timedelta(hours=hour, minutes=minute, seconds=seconds)
            random_time = (now + time_delta).replace(tzinfo=timezone.utc)

            store = random.choice(stores)
            salespeople = random.choice(Salespeople.objects.filter(store_id=store))
            ExperienceReservations.objects.create(customer=customer, store_id=store, reservation_time=random_time, salespeople=salespeople)
    
    return HttpResponse("<h1>測試資料建立完成！</h1>")