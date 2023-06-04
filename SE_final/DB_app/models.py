from django.db import models

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_gender = models.CharField(max_length=1)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    salesperson = models.ForeignKey('Salespeople', on_delete=models.CASCADE)
    referral_code = models.ForeignKey('ReferralCodes', related_name='referred_customers', on_delete=models.CASCADE)
    used_referral_code = models.ForeignKey('ReferralCodes', related_name='used_by_customers', on_delete=models.CASCADE)

class MassageChairUsages(models.Model):
    usage_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    massage_chair = models.ForeignKey('MassageChairs', on_delete=models.CASCADE)
    usage_time = models.DateTimeField()

class PhysicalStores(models.Model):
    store_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)

class PhysicalStoreDetails(models.Model):
    store = models.OneToOneField('PhysicalStores', primary_key=True, on_delete=models.CASCADE)
    store_sales = models.IntegerField()
    public_massage_chair = models.ForeignKey('MassageChairs', on_delete=models.CASCADE)

class CustomerOrders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    salesperson = models.ForeignKey('Salespeople', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    satisfaction_score = models.IntegerField()

class Salespeople(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    salesperson_name = models.CharField(max_length=255)

class ReferralCodes(models.Model):
    referral_code = models.CharField(primary_key=True, max_length=20)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_model = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

class OnlineStoreVisits(models.Model):
    visit_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    browse_source = models.CharField(max_length=255)

class PhysicalStoreSales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    customer_gender = models.CharField(max_length=1)
    customer_age = models.IntegerField()
    store = models.ForeignKey('PhysicalStores', on_delete=models.CASCADE)
    salesperson = models.ForeignKey('Salespeople', on_delete=models.CASCADE)
    sales_date = models.DateTimeField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)

class MassageChairs(models.Model):
    massage_chair_id = models.AutoField(primary_key=True)
    massage_chair_name = models.CharField(max_length=255)
    massage_chair_price = models.DecimalField(max_digits=10, decimal_places=2)