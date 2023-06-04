from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from DB_app.models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def add_data(request):
    if request.method == 'POST':
        table = request.POST.get('table')
        if table == 'customers':
            form = CustomersForm()
        elif table == 'massage_chair_usages':
            form = MassageChairUsagesForm()
        elif table == 'physical_stores':
            form = PhysicalStoresForm()
        elif table == 'physical_store_details':
            form = PhysicalStoreDetailsForm()
        elif table == 'customer_orders':
            form = CustomerOrdersForm()
        elif table == 'salespeople':
            form = SalespeopleForm()
        elif table == 'referral_codes':
            form = ReferralCodesForm()
        elif table == 'products':
            form = ProductsForm()
        elif table == 'online_store_visits':
            form = OnlineStoreVisitsForm()
        elif table == 'physical_store_sales':
            form = PhysicalStoreSalesForm()
        elif table == 'massage_chairs':
            form = MassageChairsForm()
        else:
            return HttpResponse('Invalid table name')
        return render(request, 'add_data.html', {'form': form})
    else:
        return HttpResponse('Invalid request method')
def write_test_data(request):

    #check if data exists
    if Salespeople.objects.all().exists():
        return HttpResponse('<h1>資料庫內已存在資料，尚未寫入測試資料<h1>')

    # 建立 Salespeople 測試數據
    salesperson1 = Salespeople.objects.create(salesperson_name='John')
    salesperson2 = Salespeople.objects.create(salesperson_name='Mary')
    salesperson3 = Salespeople.objects.create(salesperson_name='David')
    salesperson4 = Salespeople.objects.create(salesperson_name='Lisa')
    salesperson5 = Salespeople.objects.create(salesperson_name='Tom')
    print('成功建立 Salespeople 測試數據')

    # 建立 ReferralCodes 測試數據
    referral_code1 = ReferralCodes.objects.create(referral_code='ABC123')
    referral_code2 = ReferralCodes.objects.create(referral_code='DEF456')
    referral_code3 = ReferralCodes.objects.create(referral_code='GHI789')
    referral_code4 = ReferralCodes.objects.create(referral_code='JKL012')
    referral_code5 = ReferralCodes.objects.create(referral_code='MNO345')
    print('成功建立 ReferralCodes 測試數據')

    # 建立 Customers 測試數據
    customer1 = Customers.objects.create(customer_name='Alice', customer_gender='F', email='alice@example.com', phone_number='0912345678', salesperson=salesperson1, referral_code=referral_code1, used_referral_code=referral_code2)
    customer2 = Customers.objects.create(customer_name='Bob', customer_gender='M', email='bob@example.com', phone_number='0923456789', salesperson=salesperson2, referral_code=referral_code2, used_referral_code=referral_code3)
    customer3 = Customers.objects.create(customer_name='Cathy', customer_gender='F', email='cathy@example.com', phone_number='0934567890', salesperson=salesperson3, referral_code=referral_code3, used_referral_code=referral_code4)
    customer4 = Customers.objects.create(customer_name='David', customer_gender='M', email='david@example.com', phone_number='0945678901', salesperson=salesperson4, referral_code=referral_code4, used_referral_code=referral_code5)
    customer5 = Customers.objects.create(customer_name='Emily', customer_gender='F', email='emily@example.com', phone_number='0956789012', salesperson=salesperson5, referral_code=referral_code5, used_referral_code=referral_code1)
    print('成功建立 Customers 測試數據')

    # 建立 MassageChairs 測試數據
    massage_chair1 = MassageChairs.objects.create(massage_chair_name='Model A', massage_chair_price=10000)
    massage_chair2 = MassageChairs.objects.create(massage_chair_name='Model B', massage_chair_price=20000)
    massage_chair3 = MassageChairs.objects.create(massage_chair_name='Model C', massage_chair_price=30000)
    massage_chair4 = MassageChairs.objects.create(massage_chair_name='Model D', massage_chair_price=40000)
    massage_chair5 = MassageChairs.objects.create(massage_chair_name='Model E', massage_chair_price=50000)
    print('成功建立 MassageChairs 測試數據')

    # 建立 MassageChairUsages 測試數據
    usage1 = MassageChairUsages.objects.create(customer=customer1, massage_chair=massage_chair1, usage_time=timezone.now())
    usage2 = MassageChairUsages.objects.create(customer=customer2, massage_chair=massage_chair2, usage_time=timezone.now() - timedelta(days=1))
    usage3 = MassageChairUsages.objects.create(customer=customer3, massage_chair=massage_chair3, usage_time=timezone.now() - timedelta(days=2))
    usage4 = MassageChairUsages.objects.create(customer=customer4, massage_chair=massage_chair4, usage_time=timezone.now() - timedelta(days=3))
    usage5 = MassageChairUsages.objects.create(customer=customer5, massage_chair=massage_chair5, usage_time=timezone.now() - timedelta(days=4))
    print('成功建立 MassageChairUsages 測試數據')

    # 建立 PhysicalStores 測試數據
    store1 = PhysicalStores.objects.create(branch_name='Store A')
    store2 = PhysicalStores.objects.create(branch_name='Store B')
    store3 = PhysicalStores.objects.create(branch_name='Store C')
    store4 = PhysicalStores.objects.create(branch_name='Store D')
    store5 = PhysicalStores.objects.create(branch_name='Store E')
    print('成功建立 PhysicalStores 測試數據')

    # 建立 PhysicalStoreDetails 測試數據
    store_detail1 = PhysicalStoreDetails.objects.create(store=store1, store_sales=100000, public_massage_chair=massage_chair1)
    store_detail2 = PhysicalStoreDetails.objects.create(store=store2, store_sales=200000, public_massage_chair=massage_chair2)
    store_detail3 = PhysicalStoreDetails.objects.create(store=store3, store_sales=300000, public_massage_chair=massage_chair3)
    store_detail4 = PhysicalStoreDetails.objects.create(store=store4, store_sales=400000, public_massage_chair=massage_chair4)
    store_detail5 = PhysicalStoreDetails.objects.create(store=store5, store_sales=500000, public_massage_chair=massage_chair5)
    print('成功建立 PhysicalStoreDetails 測試數據')

    # 建立 Products 測試數據
    product1 = Products.objects.create(product_model='Model A', product_name='Product A', product_price=1000)
    product2 = Products.objects.create(product_model='Model B', product_name='Product B', product_price=2000)
    product3 = Products.objects.create(product_model='Model C', product_name='Product C', product_price=3000)
    product4 = Products.objects.create(product_model='Model D', product_name='Product D', product_price=4000)
    product5 = Products.objects.create(product_model='Model E', product_name='Product E', product_price=5000)
    print('成功建立 Products 測試數據')

    # 建立 CustomerOrders 測試數據
    order1 = CustomerOrders.objects.create(customer=customer1, product=product1, salesperson=salesperson1, order_date=timezone.now(), satisfaction_score=5)
    order2 = CustomerOrders.objects.create(customer=customer2, product=product2, salesperson=salesperson2, order_date=timezone.now() - timedelta(days=1), satisfaction_score=4)
    order3 = CustomerOrders.objects.create(customer=customer3, product=product3, salesperson=salesperson3, order_date=timezone.now() - timedelta(days=2), satisfaction_score=3)
    order4 = CustomerOrders.objects.create(customer=customer4, product=product4, salesperson=salesperson4, order_date=timezone.now() - timedelta(days=3), satisfaction_score=2)
    order5 = CustomerOrders.objects.create(customer=customer5, product=product5, salesperson=salesperson5, order_date=timezone.now() - timedelta(days=4), satisfaction_score=1)
    print('成功建立 CustomerOrders 測試數據')

    # 建立 OnlineStoreVisits 測試數據
    visit1 = OnlineStoreVisits.objects.create(customer=customer1, browse_source='Google')
    visit2 = OnlineStoreVisits.objects.create(customer=customer2, browse_source='Facebook')
    visit3 = OnlineStoreVisits.objects.create(customer=customer3, browse_source='Instagram')
    visit4 = OnlineStoreVisits.objects.create(customer=customer4, browse_source='Twitter')
    visit5 = OnlineStoreVisits.objects.create(customer=customer5, browse_source='LinkedIn')
    print('成功建立 OnlineStoreVisits 測試數據')

    # 建立 PhysicalStoreSales 測試數據
    sales1 = PhysicalStoreSales.objects.create(customer=customer1, customer_gender='F', customer_age=30, store=store1, salesperson=salesperson1, sales_date=timezone.now(), order_total=1000)
    sales2 = PhysicalStoreSales.objects.create(customer=customer2, customer_gender='M', customer_age=40, store=store2, salesperson=salesperson2, sales_date=timezone.now() - timedelta(days=1), order_total=2000)
    sales3 = PhysicalStoreSales.objects.create(customer=customer3, customer_gender='F', customer_age=50, store=store3, salesperson=salesperson3, sales_date=timezone.now() - timedelta(days=2), order_total=3000)
    sales4 = PhysicalStoreSales.objects.create(customer=customer4, customer_gender='M', customer_age=60, store=store4, salesperson=salesperson4, sales_date=timezone.now() - timedelta(days=3), order_total=4000)
    sales5 = PhysicalStoreSales.objects.create(customer=customer5, customer_gender='F', customer_age=70, store=store5, salesperson=salesperson5, sales_date=timezone.now() - timedelta(days=4), order_total=5000)
    print('成功建立 PhysicalStoreSales 測試數據')
    print('所有資料庫測試數據載入成功！')

    return HttpResponse('<h1>所有資料庫測試數據載入成功！</h1>')