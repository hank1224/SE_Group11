from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

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
        return HttpResponse("<h1>已建立過測試資料</h1>")

    # 首先，我們需要確定所有的外建約束在測試資料中也一定要存在。
    # PhysicalStores 先建立一些店鋪：
    store1 = PhysicalStores.objects.create(branch_name="實體店A")
    store2 = PhysicalStores.objects.create(branch_name="實體店B")
    store3 = PhysicalStores.objects.create(branch_name="實體店C")
    store4 = PhysicalStores.objects.create(branch_name="實體店D")
    store5 = PhysicalStores.objects.create(branch_name="實體店E")

    # Salespeople 在每個店鋪中新增銷售員：
    staff1 = User.objects.create_user(
        username="staff1",
        password="testpassword",
        is_staff=True
    )
    salespeople1 = Salespeople.objects.create(salesperson_name="銷售員1", store_id=store1, staff_username=staff1)

    staff2 = User.objects.create_user(
        username="staff2",
        password="testpassword",
        is_staff=True
    )
    salespeople2 = Salespeople.objects.create(salesperson_name="銷售員2", store_id=store5, staff_username=staff2)

    staff3 = User.objects.create_user(
        username="staff3",
        password="testpassword",
        is_staff=True
    )
    salespeople3 = Salespeople.objects.create(salesperson_name="銷售員3", store_id=store2, staff_username=staff3)

    staff4 = User.objects.create_user(
        username="staff4",
        password="testpassword",
        is_staff=True
    )
    salespeople4 = Salespeople.objects.create(salesperson_name="銷售員4", store_id=store3, staff_username=staff4)

    staff5 = User.objects.create_user(
        username="staff5",
        password="testpassword",
        is_staff=True
    )
    salespeople5 = Salespeople.objects.create(salesperson_name="銷售員5", store_id=store4, staff_username=staff5)
    

    # Products 建立產品：
    prod1 = Products.objects.create(product_model="HY-3068A", product_name="WULA超有力小沙發按摩椅", product_price=25000, product_cost=20000, product_warranty=False)
    prod2 = Products.objects.create(product_model="HY-5083", product_name="追夢椅PLUS(石墨烯升級款)", product_price=72000, product_cost=50000, product_warranty=True)
    prod3 = Products.objects.create(product_model="HY-5082A", product_name="V-Motion一健椅", product_price=108000, product_cost=80000, product_warranty=True)
    prod4 = Products.objects.create(product_model="HY-5013", product_name="商務艙PLUS零重力按摩椅", product_price=39000, product_cost=30000, product_warranty=False)
    prod5 = Products.objects.create(product_model="HY-CR52-GY", product_name="樂享起身沙發椅 (多功能電動沙發/起身椅)", product_price=15000, product_cost=10000, product_warranty=False)    

    # Customers：

    #user1
    user1 = User.objects.create_user(
        username="user1",
        password="testpassword"
    )
    cust1 = Customers.objects.create(
        username=user1,
        customer_name="顧客1",
        customer_gender="1",
        phone_number="0912345678",
        salesperson=salespeople1
    )

    #user2
    user2 = User.objects.create_user(
        username="user2",
        password="testpassword"
    )
    cust2 = Customers.objects.create(
        username=user2,
        customer_name="顧客2",
        customer_gender="2",
        phone_number="0987654321",
        salesperson=salespeople2
    )

    #user3
    user3 = User.objects.create_user(
        username="user3",
        password="testpassword"
    )
    cust3 = Customers.objects.create(
        username=user3,
        customer_name="顧客3",
        customer_gender="1",
        phone_number="0912345678",
        salesperson=salespeople1
    )

    #user4
    user4 = User.objects.create_user(
        username="user4",
        password="testpassword"
    )
    cust4 = Customers.objects.create(
        username=user4,
        customer_name="顧客4",
        customer_gender="3",
        phone_number="0987654321",
        salesperson=salespeople4
    )

    #user5
    user5 = User.objects.create_user(
        username="user5",
        password="testpassword"
    )
    cust5 = Customers.objects.create(
        username=user5,
        customer_name="顧客5",
        customer_gender="4",
        phone_number="0912345678",
        salesperson=salespeople1
    )
    
    # user6
    user6 = User.objects.create_user(
        username="user6",
        password="testpassword"
    )
    cust6 = Customers.objects.create(
        username=user6,
        customer_name="顧客6",
        customer_gender="4",
        phone_number="0987654321",
        salesperson=salespeople5
    )

    # user7
    user7 = User.objects.create_user(
        username="user7",
        password="testpassword"
    )
    cust7 = Customers.objects.create(
        username=user7,
        customer_name="顧客7",
        customer_gender="4",
        phone_number="0912345678",
        salesperson=salespeople1
    )

    # user8
    user8 = User.objects.create_user(
        username="user8",
        password="testpassword"
    )
    cust8 = Customers.objects.create(
        username=user8,
        customer_name="顧客8",
        customer_gender="3",
        phone_number="0987654321",
        salesperson=salespeople4
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
    customers = [cust1, cust2, cust3, cust4, cust5, cust6, cust7, cust8]
    massage_chairs = [chair1, chair2, chair3, chair4, chair5]
    modes = [mode1, mode2, mode3, mode4, mode5]
    payments = ['1', '2']

    # 建立25筆按摩椅紀錄
    for i in range(25):
        customer = random.choice(customers)
        massage_chair = random.choice(massage_chairs)
        massage_chair_mode = random.choice(modes)
        payment = random.choice(payments)
        
        record = MassageChairRecord.objects.create(customer=customer, massage_chair=massage_chair, 
                                                massage_chair_mode=massage_chair_mode, payment=payment)
        record.save()
    

    # CustomerWebViews 建立線上商店參觀紀錄：
    for i in range(25):
        cust = random.choice([cust1, cust2, cust3, cust4, cust5, cust6, cust7, cust8])
        prod = random.choice([prod1, prod2, prod3, prod4, prod5])
        visit = CustomerWebViews.objects.create(customer=cust, product=prod)
    

    # SalesRecords 建立銷售紀錄：
    for i in range(50):
        cust = random.choice([cust1, cust2, cust3, cust4, cust5, cust6, cust7, cust8])
        prod = random.choice([prod1, prod2, prod3, prod4, prod5])
        sales_type = random.choice(["1", "2"])
        if sales_type == "1":
            store = None
            sales_price = Products.objects.get(product_id=prod.product_id).product_price
        else:
            store = random.choice([store1, store2, store3])
        salesperson = random.choice([salespeople1, salespeople2, salespeople3, salespeople4, salespeople5])
        orgin_price = Products.objects.get(product_id=prod.product_id).product_price
        addion = random.randint(1, 30)*100
        sales_price = orgin_price + addion
        SalesRecords.objects.create(customer=cust, product=prod, sales_type=sales_type, salesperson=salesperson, store=store, sales_price=sales_price)

    # ReferralCodes 建立推薦序號：
    referral1 = ReferralCodes.objects.create(customer=cust1, referral_code="341234", used_referral_code="")
    referral2 = ReferralCodes.objects.create(customer=cust2, referral_code="823581", used_referral_code="341234")
    referral3 = ReferralCodes.objects.create(customer=cust3, referral_code="745634", used_referral_code="")
    referral4 = ReferralCodes.objects.create(customer=cust4, referral_code="123876", used_referral_code="")
    referral5 = ReferralCodes.objects.create(customer=cust5, referral_code="465312", used_referral_code="341234")
    referral6 = ReferralCodes.objects.create(customer=cust6, referral_code="786234", used_referral_code="")
    referral7 = ReferralCodes.objects.create(customer=cust7, referral_code="321567", used_referral_code="")
    referral8 = ReferralCodes.objects.create(customer=cust8, referral_code="489561", used_referral_code="745634")
    
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
    for customer in customers:
        hour = random.randint(0, 99)
        minute = random.randrange(0, 4) * 15
        seconds = 0
        time_delta = datetime.timedelta(hours=hour, minutes=minute, seconds=seconds)
        random_time = (now + time_delta).replace(tzinfo=timezone.utc)

        store = random.choice(stores)
        salespeople = random.choice(Salespeople.objects.filter(store_id=store))
        ExperienceReservations.objects.create(customer=customer, store_id=store, reservation_time=random_time, salespeople=salespeople)

    return HttpResponse("測試資料建立完成！")