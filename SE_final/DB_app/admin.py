from django.contrib import admin
from DB_app.models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_gender', 'email', 'phone_number', 'salesperson')
    list_filter = ('customer_gender', 'salesperson')

class MassageChairRecordAdmin(admin.ModelAdmin):
    list_display = ('usage_id', 'customer', 'massage_chair', 'massage_chair_mode', 'start_time')
    list_filter = ('massage_chair', 'massage_chair_mode')

class PhysicalStoresAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'branch_name')

class MassageChairPhysicalStoresAdmin(admin.ModelAdmin):
    list_display = ('store', 'public_massage_chair')
    list_filter = ('store',)

class SalespeopleAdmin(admin.ModelAdmin):
    list_display = ('salesperson_id', 'salesperson_name', 'store_id')
    list_filter = ('store_id',)

class ReferralCodesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'referral_code', 'uesd_referral_code')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_model', 'product_name', 'product_price', 'product_cost', 'product_warranty', 'product_warranty_period')
    list_filter = ('product_warranty',)

class OnlineStoreVisitsAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'customer', 'product')

class MassageChairsAdmin(admin.ModelAdmin):
    list_display = ('massage_chair_id', 'massage_chair_name', 'massage_chair_price')

class MassageChairModesAdmin(admin.ModelAdmin):
    list_display = ('massage_chair_mode_id', 'massage_chair_mode_name')

class SalesRecordsAdmin(admin.ModelAdmin):
    list_display = ('sales_record_id', 'customer', 'product', 'sales_time', 'sales_type', 'salesperson', 'store', 'sales_price')
    list_filter = ('sales_time', 'sales_type', 'store__branch_name')

class SalesQuestionnairesAdmin(admin.ModelAdmin):
    list_display = ('sales_record', 'sales_process_score', 'warranty_process_score')

admin.site.register(Customers, CustomersAdmin)
admin.site.register(MassageChairRecord, MassageChairRecordAdmin)
admin.site.register(PhysicalStores, PhysicalStoresAdmin)
admin.site.register(MassageChairPhysicalStores, MassageChairPhysicalStoresAdmin)
admin.site.register(Salespeople, SalespeopleAdmin)
admin.site.register(ReferralCodes, ReferralCodesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(OnlineStoreVisits, OnlineStoreVisitsAdmin)
admin.site.register(MassageChairs, MassageChairsAdmin)
admin.site.register(MassageChairModes, MassageChairModesAdmin)
admin.site.register(SalesRecords, SalesRecordsAdmin)
admin.site.register(SalesQuestionnaires, SalesQuestionnairesAdmin)