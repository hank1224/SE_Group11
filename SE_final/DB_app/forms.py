from django import forms
from .models import *

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['customer_name', 'customer_gender', 'email', 'phone_number', 'salesperson', 'referral_code', 'used_referral_code']

class MassageChairUsagesForm(forms.ModelForm):
    class Meta:
        model = MassageChairUsages
        fields = ['customer', 'massage_chair', 'usage_time']

class PhysicalStoresForm(forms.ModelForm):
    class Meta:
        model = PhysicalStores
        fields = ['branch_name']

class PhysicalStoreDetailsForm(forms.ModelForm):
    class Meta:
        model = PhysicalStoreDetails
        fields = ['store', 'store_sales', 'public_massage_chair']

class CustomerOrdersForm(forms.ModelForm):
    class Meta:
        model = CustomerOrders
        fields = ['customer', 'product', 'salesperson', 'order_date', 'satisfaction_score']

class SalespeopleForm(forms.ModelForm):
    class Meta:
        model = Salespeople
        fields = ['salesperson_name']

class ReferralCodesForm(forms.ModelForm):
    class Meta:
        model = ReferralCodes
        fields = ['referral_code']

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_model', 'product_name', 'product_price']

class OnlineStoreVisitsForm(forms.ModelForm):
    class Meta:
        model = OnlineStoreVisits
        fields = ['customer', 'browse_source']

class PhysicalStoreSalesForm(forms.ModelForm):
    class Meta:
        model = PhysicalStoreSales
        fields = ['customer', 'customer_gender', 'customer_age', 'store', 'salesperson', 'sales_date', 'order_total']

class MassageChairsForm(forms.ModelForm):
    class Meta:
        model = MassageChairs
        fields = ['massage_chair_name', 'massage_chair_price']