from django.db import models

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    # 顧客性別 [1:男 2:女 3:其他 4:不願透漏]
    GENDER_CHOICES = [
        ('1', '男'),
        ('2', '女'),
        ('3', '其他'),
        ('4', '不願透漏'),
    ]
    customer_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    salesperson = models.ForeignKey('Salespeople', on_delete=models.CASCADE)

class MassageChairRecord(models.Model):
    usage_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    massage_chair = models.ForeignKey('MassageChairs', on_delete=models.CASCADE)
    massage_chair_mode = models.ForeignKey('MassageChairModes', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)

class PhysicalStores(models.Model):
    store_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)

class MassageChairPhysicalStores(models.Model):
    store = models.OneToOneField('PhysicalStores', primary_key=True, on_delete=models.CASCADE)
    public_massage_chair = models.ForeignKey('MassageChairs', on_delete=models.CASCADE)

class Salespeople(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    salesperson_name = models.CharField(max_length=255)
    store_id = models.ForeignKey('PhysicalStores', on_delete=models.CASCADE)

class ReferralCodes(models.Model):
    customer = models.OneToOneField('Customers', on_delete=models.CASCADE)
    referral_code = models.CharField(primary_key=True, max_length=20)
    uesd_referral_code = models.CharField(max_length=20)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_model = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_warranty = models.BooleanField(default=False)
    product_warranty_period = models.DurationField(default=0)

class OnlineStoreVisits(models.Model):
    visit_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)

class MassageChairs(models.Model):
    massage_chair_id = models.AutoField(primary_key=True)
    massage_chair_name = models.CharField(max_length=255)
    massage_chair_price = models.DecimalField(max_digits=10, decimal_places=2)

class MassageChairModes(models.Model):
    massage_chair_mode_id = models.AutoField(primary_key=True)
    massage_chair_mode_name = models.CharField(max_length=255)

class SalesRecords(models.Model):
    sales_record_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    sales_time = models.DateTimeField(auto_now_add=True)
    SALES_TYPE_CHOICES = [
        ('1', '線上'),
        ('2', '實體'),
    ]
    sales_type = models.CharField(max_length=1, choices=SALES_TYPE_CHOICES)

    # 實體店面使用以下欄位
    salesperson = models.ForeignKey('Salespeople', on_delete=models.CASCADE)
    store = models.ForeignKey('PhysicalStores', on_delete=models.CASCADE)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class SalesQuestionnaires(models.Model):
    sales_record = models.OneToOneField('SalesRecords', primary_key=True, on_delete=models.CASCADE)
    sales_process_score = models.IntegerField(default=None)
    warranty_process_score = models.IntegerField(default=None)