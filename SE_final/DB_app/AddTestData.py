""" !!!此檔無效!!! """
""" !!!此檔無效!!! """
""" !!!此檔無效!!! """

from django.contrib.auth.models import User
from django.utils import timezone
from random import randint, choice
from .models import *


"""
python manage.py shell

你可以在Django shell中執行這些函數，例如：

```python
>>> from DB_app.AddTestData import *
>>> generate_customers(10)
>>> generate_physical_stores(3)
>>> generate_salespeople(5)
>>> generate_products(10)
>>> generate_massage_chairs(5)
>>> generate_massage_chair_modes(3)
>>> generate_massage_chair_physical_stores(3)
>>> generate_sales_records(20)
>>> generate_massage_chair_records(10)
>>> generate_online_store_visits(30)
>>> generate_sales_questionnaires(10)
``` 

這樣就可以生成10個顧客、3個實體店面、5個銷售員、10個產品、
5張按摩椅、3種按摩椅模式、3個按摩椅實體店面、20筆銷售記錄、10筆按摩椅使用記錄、
30次線上商店訪問和10份銷售問卷。
"""

def generate_customers(num):
    for i in range(num):
        customer = Customers.objects.create(
            customer_name=f"Customer {i+1}",
            customer_gender=choice(['1', '2', '3', '4']),
            email=f"customer{i+1}@example.com",
            phone_number=f"09{randint(10000000, 99999999)}",
        )
        ReferralCodes.objects.create(
            customer=customer,
            referral_code=f"REF{i+1}",
            uesd_referral_code=f"REF{randint(1, i)}",
        )

def generate_physical_stores(num):
    for i in range(num):
        PhysicalStores.objects.create(
            branch_name=f"Store {i+1}",
        )

def generate_salespeople(num):
    stores = PhysicalStores.objects.all()
    for i in range(num):
        Salespeople.objects.create(
            salesperson_name=f"Salesperson {i+1}",
            store_id=choice(stores),
        )

def generate_products(num):
    for i in range(num):
        Products.objects.create(
            product_model=f"Model {i+1}",
            product_name=f"Product {i+1}",
            product_price=randint(1000, 10000),
            product_cost=randint(500, 5000),
            product_warranty=bool(randint(0, 1)),
            product_warranty_period=timezone.timedelta(days=randint(30, 365)),
        )

def generate_massage_chairs(num):
    for i in range(num):
        MassageChairs.objects.create(
            massage_chair_name=f"Massage Chair {i+1}",
            massage_chair_price=randint(10000, 50000),
        )

def generate_massage_chair_modes(num):
    for i in range(num):
        MassageChairModes.objects.create(
            massage_chair_mode_name=f"Mode {i+1}",
        )

def generate_massage_chair_physical_stores(num):
    stores = PhysicalStores.objects.all()
    chairs = MassageChairs.objects.all()
    for i in range(num):
        MassageChairPhysicalStores.objects.create(
            store=choice(stores),
            public_massage_chair=choice(chairs),
        )

def generate_sales_records(num):
    customers = Customers.objects.all()
    products = Products.objects.all()
    salespeople = Salespeople.objects.all()
    stores = PhysicalStores.objects.all()
    for i in range(num):
        SalesRecords.objects.create(
            customer=choice(customers),
            product=choice(products),
            sales_time=timezone.now(),
            sales_type=choice(['1', '2']),
            salesperson=choice(salespeople),
            store=choice(stores),
            sales_price=randint(1000, 10000),
        )

def generate_massage_chair_records(num):
    customers = Customers.objects.all()
    chairs = MassageChairs.objects.all()
    modes = MassageChairModes.objects.all()
    for i in range(num):
        MassageChairRecord.objects.create(
            customer=choice(customers),
            massage_chair=choice(chairs),
            massage_chair_mode=choice(modes),
            start_time=timezone.now(),
        )

def generate_online_store_visits(num):
    customers = Customers.objects.all()
    products = Products.objects.all()
    for i in range(num):
        OnlineStoreVisits.objects.create(
            customer=choice(customers),
            product=choice(products),
        )

def generate_sales_questionnaires(num):
    records = SalesRecords.objects.all()
    for i in range(num):
        SalesQuestionnaires.objects.create(
            sales_record=choice(records),
            sales_process_score=randint(1, 10),
            warranty_process_score=randint(1, 10),
        )