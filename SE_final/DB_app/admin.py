from django.contrib import admin
from DB_app.models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_name', 'customer_gender', 'email', 'phone_number', 'salesperson', 'referral_code', 'used_referral_code']
    search_fields = ['customer_name', 'phone_number']
    list_filter = ['customer_gender', 'salesperson']
    ordering = ['customer_id']

class MassageChairUsagesAdmin(admin.ModelAdmin):
    list_display = ['usage_id', 'customer', 'massage_chair', 'usage_time']
    search_fields = ['customer__customer_name', 'massage_chair__massage_chair_name']
    ordering = ['usage_id']

class PhysicalStoresAdmin(admin.ModelAdmin):
    list_display = ['store_id', 'branch_name']

class PhysicalStoreDetailsAdmin(admin.ModelAdmin):
    list_display = ['store', 'store_sales', 'public_massage_chair']

class CustomerOrdersAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer', 'product', 'salesperson', 'order_date', 'satisfaction_score']
    search_fields = ['customer__customer_name', 'product__product_name', 'salesperson__salesperson_name']
    list_filter = ['salesperson']
    ordering = ['order_id']

class SalespeopleAdmin(admin.ModelAdmin):
    list_display = ['salesperson_id', 'salesperson_name']
    search_fields = ['salesperson_name']
    ordering = ['salesperson_id']

class ReferralCodesAdmin(admin.ModelAdmin):
    list_display = ['referral_code']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_model', 'product_name', 'product_price']
    search_fields = ['product_name']
    ordering = ['product_id']

class OnlineStoreVisitsAdmin(admin.ModelAdmin):
    list_display = ['visit_id', 'customer', 'browse_source']
    search_fields = ['customer__customer_name']
    ordering = ['visit_id']

class PhysicalStoreSalesAdmin(admin.ModelAdmin):
    list_display = ['sales_id', 'customer', 'customer_gender', 'customer_age', 'store', 'salesperson', 'sales_date', 'order_total']
    search_fields = ['customer__customer_name', 'store__branch_name', 'salesperson__salesperson_name']
    list_filter = ['customer_gender', 'salesperson']
    ordering = ['sales_id']

class MassageChairsAdmin(admin.ModelAdmin):
    list_display = ['massage_chair_id', 'massage_chair_name', 'massage_chair_price']
    search_fields = ['massage_chair_name']
    ordering = ['massage_chair_id']

admin.site.register(Customers, CustomersAdmin)
admin.site.register(MassageChairUsages, MassageChairUsagesAdmin)
admin.site.register(PhysicalStores, PhysicalStoresAdmin)
admin.site.register(PhysicalStoreDetails, PhysicalStoreDetailsAdmin)
admin.site.register(CustomerOrders, CustomerOrdersAdmin)
admin.site.register(Salespeople, SalespeopleAdmin)
admin.site.register(ReferralCodes, ReferralCodesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(OnlineStoreVisits, OnlineStoreVisitsAdmin)
admin.site.register(PhysicalStoreSales, PhysicalStoreSalesAdmin)
admin.site.register(MassageChairs, MassageChairsAdmin)