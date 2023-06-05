from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Customers, MassageChairRecord, PhysicalStores, MassageChairPhysicalStores, Salespeople, ReferralCodes, Products, OnlineStoreVisits, MassageChairs, MassageChairModes, SalesRecords, SalesQuestionnaires

def index(request):
    return render(request, 'index.html')

def create_test_data(request):
    # 建立實體店面資料
    physical_store1 = PhysicalStores.objects.create(branch_name='Store A')
    physical_store2 = PhysicalStores.objects.create(branch_name='Store B')
    physical_store3 = PhysicalStores.objects.create(branch_name='Store C')
    physical_store4 = PhysicalStores.objects.create(branch_name='Store D')
    physical_store5 = PhysicalStores.objects.create(branch_name='Store E')
    print("建立實體店面資料")

    # 建立業務人員資料
    salesperson1 = Salespeople.objects.create(salesperson_name='Jack', store_id=physical_store1)
    salesperson2 = Salespeople.objects.create(salesperson_name='Rose', store_id=physical_store2)
    salesperson3 = Salespeople.objects.create(salesperson_name='David', store_id=physical_store3)
    salesperson4 = Salespeople.objects.create(salesperson_name='Amy', store_id=physical_store4)
    salesperson5 = Salespeople.objects.create(salesperson_name='Bob', store_id=physical_store5)
    print("建立業務人員資料")

    # 建立顧客資料
    customer1 = Customers.objects.create(customer_name='John', customer_gender='1', email='john@example.com', phone_number='0912345678', salesperson=salesperson1)
    customer2 = Customers.objects.create(customer_name='Mary', customer_gender='2', email='mary@example.com', phone_number='0923456789', salesperson=salesperson2)
    customer3 = Customers.objects.create(customer_name='Tom', customer_gender='1', email='tom@example.com', phone_number='0934567890', salesperson=salesperson3)
    customer4 = Customers.objects.create(customer_name='Jane', customer_gender='2', email='jane@example.com', phone_number='0945678901', salesperson=salesperson4)
    customer5 = Customers.objects.create(customer_name='Peter', customer_gender='1', email='peter@example.com', phone_number='0956789012', salesperson=salesperson5)
    print("建立顧客資料")

    # 建立按摩椅使用紀錄資料
    massage_chair1 = MassageChairs.objects.create(massage_chair_name='Massage Chair A', massage_chair_price=10000)
    massage_chair2 = MassageChairs.objects.create(massage_chair_name='Massage Chair B', massage_chair_price=20000)
    massage_chair3 = MassageChairs.objects.create(massage_chair_name='Massage Chair C', massage_chair_price=30000)
    massage_chair_mode1 = MassageChairModes.objects.create(massage_chair_mode_name='Mode 1')
    massage_chair_mode2 = MassageChairModes.objects.create(massage_chair_mode_name='Mode 2')
    massage_chair_record1 = MassageChairRecord.objects.create(customer=customer1, massage_chair=massage_chair1, massage_chair_mode=massage_chair_mode1, start_time=timezone.now())
    massage_chair_record2 = MassageChairRecord.objects.create(customer=customer2, massage_chair=massage_chair2, massage_chair_mode=massage_chair_mode2, start_time=timezone.now())
    massage_chair_record3 = MassageChairRecord.objects.create(customer=customer3, massage_chair=massage_chair3, massage_chair_mode=massage_chair_mode1, start_time=timezone.now())
    massage_chair_record4 = MassageChairRecord.objects.create(customer=customer4, massage_chair=massage_chair1, massage_chair_mode=massage_chair_mode2, start_time=timezone.now())
    massage_chair_record5 = MassageChairRecord.objects.create(customer=customer5, massage_chair=massage_chair2, massage_chair_mode=massage_chair_mode1, start_time=timezone.now())
    print("建立按摩椅使用紀錄資料")

    # 建立按摩椅與實體店面關聯資料
    massage_chair_physical_store1 = MassageChairPhysicalStores.objects.create(store=physical_store1, public_massage_chair=massage_chair1)
    massage_chair_physical_store2 = MassageChairPhysicalStores.objects.create(store=physical_store2, public_massage_chair=massage_chair2)
    massage_chair_physical_store3 = MassageChairPhysicalStores.objects.create(store=physical_store3, public_massage_chair=massage_chair3)
    massage_chair_physical_store4 = MassageChairPhysicalStores.objects.create(store=physical_store4, public_massage_chair=massage_chair1)
    massage_chair_physical_store5 = MassageChairPhysicalStores.objects.create(store=physical_store5, public_massage_chair=massage_chair2)
    print("建立按摩椅與實體店面關聯資料")

    # 建立推薦碼資料
    referral_code1 = ReferralCodes.objects.create(customer=customer1, referral_code='REF001', uesd_referral_code='')
    referral_code2 = ReferralCodes.objects.create(customer=customer2, referral_code='REF002', uesd_referral_code='')
    referral_code3 = ReferralCodes.objects.create(customer=customer3, referral_code='REF003', uesd_referral_code='')
    referral_code4 = ReferralCodes.objects.create(customer=customer4, referral_code='REF004', uesd_referral_code='')
    referral_code5 = ReferralCodes.objects.create(customer=customer5, referral_code='REF005', uesd_referral_code='')
    print("建立推薦碼資料")

    # 建立產品資料
    product1 = Products.objects.create(product_model='Product A', product_name='Product A', product_price=1000, product_cost=500, product_warranty=True, product_warranty_period=timezone.timedelta(days=365))
    product2 = Products.objects.create(product_model='Product B', product_name='Product B', product_price=2000, product_cost=1000, product_warranty=True, product_warranty_period=timezone.timedelta(days=365))
    product3 = Products.objects.create(product_model='Product C', product_name='Product C', product_price=3000, product_cost=1500, product_warranty=True, product_warranty_period=timezone.timedelta(days=365))
    product4 = Products.objects.create(product_model='Product D', product_name='Product D', product_price=4000, product_cost=2000, product_warranty=True, product_warranty_period=timezone.timedelta(days=365))
    product5 = Products.objects.create(product_model='Product E', product_name='Product E', product_price=5000, product_cost=2500, product_warranty=True, product_warranty_period=timezone.timedelta(days=365))
    print("建立產品資料")

    # 建立線上商店訪問資料
    online_store_visit1 = OnlineStoreVisits.objects.create(customer=customer1, product=product1)
    online_store_visit2 = OnlineStoreVisits.objects.create(customer=customer2, product=product2)
    online_store_visit3 = OnlineStoreVisits.objects.create(customer=customer3, product=product3)
    online_store_visit4 = OnlineStoreVisits.objects.create(customer=customer4, product=product4)
    online_store_visit5 = OnlineStoreVisits.objects.create(customer=customer5, product=product5)
    print("建立線上商店訪問資料")

    # 建立銷售紀錄資料
    sales_record1 = SalesRecords.objects.create(customer=customer1, product=product1, sales_time=timezone.now(), sales_type='1')
    sales_record2 = SalesRecords.objects.create(customer=customer2, product=product2, sales_time=timezone.now(), sales_type='1')
    sales_record3 = SalesRecords.objects.create(customer=customer3, product=product3, sales_time=timezone.now(), sales_type='1')
    sales_record4 = SalesRecords.objects.create(customer=customer4, product=product4, sales_time=timezone.now(), sales_type='1')
    sales_record5 = SalesRecords.objects.create(customer=customer5, product=product5, sales_time=timezone.now(), sales_type='1')
    print("建立銷售紀錄資料")

    # 建立實體店面銷售紀錄資料
    sales_record6 = SalesRecords.objects.create(customer=customer1, product=product1, sales_time=timezone.now(), sales_type='2', salesperson=salesperson1, store=physical_store1, sales_price=1200)
    sales_record7 = SalesRecords.objects.create(customer=customer2, product=product2, sales_time=timezone.now(), sales_type='2', salesperson=salesperson2, store=physical_store2, sales_price=2200)
    sales_record8 = SalesRecords.objects.create(customer=customer3, product=product3, sales_time=timezone.now(), sales_type='2', salesperson=salesperson3, store=physical_store3, sales_price=3200)
    sales_record9 = SalesRecords.objects.create(customer=customer4, product=product4, sales_time=timezone.now(), sales_type='2', salesperson=salesperson4, store=physical_store4, sales_price=4200)
    sales_record10 = SalesRecords.objects.create(customer=customer5, product=product5, sales_time=timezone.now(), sales_type='2', salesperson=salesperson5, store=physical_store5, sales_price=5200)
    print("建立實體店面銷售紀錄資料")

    # 建立銷售問卷資料
    sales_questionnaire1 = SalesQuestionnaires.objects.create(sales_record=sales_record1, sales_process_score=5, warranty_process_score=2)
    sales_questionnaire2 = SalesQuestionnaires.objects.create(sales_record=sales_record2, sales_process_score=1, warranty_process_score=5)
    sales_questionnaire3 = SalesQuestionnaires.objects.create(sales_record=sales_record3, sales_process_score=3, warranty_process_score=4)
    sales_questionnaire4 = SalesQuestionnaires.objects.create(sales_record=sales_record4, sales_process_score=1, warranty_process_score=1)
    sales_questionnaire5 = SalesQuestionnaires.objects.create(sales_record=sales_record5, sales_process_score=5, warranty_process_score=1)
    print("建立銷售問卷資料")

    return HttpResponse('<h1>資料建立完成</h1>')