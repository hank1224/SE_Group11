from django.contrib import admin
from DB_app.models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_gender', 'phone_number', 'salesperson')
    list_filter = ('customer_gender', 'salesperson')

class MassageChairRecordAdmin(admin.ModelAdmin):
    list_display = ('usage_id', 'customer', 'massage_chair', 'massage_chair_mode', 'start_time', 'payment')
    list_filter = ('payment',)

class PhysicalStoresAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'branch_name')

class ReferralCodesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'referral_code', 'used_referral_code')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_model', 'product_name', 'product_price', 'product_cost', 'product_warranty')

class OnlineStoreVisitsAdmin(admin.ModelAdmin):
    list_display = ('visit_id', 'customer', 'product')

class MassageChairsAdmin(admin.ModelAdmin):
    list_display = ('massage_chair_id', 'store_id', 'product_model')

class MassageChairModesAdmin(admin.ModelAdmin):
    list_display = ('massage_chair_mode_id', 'massage_chair_mode_name')

class SalesRecordsAdmin(admin.ModelAdmin):
    list_display = ('sales_record_id', 'customer', 'product', 'sales_time', 'sales_type', 'salesperson', 'store', 'sales_price')
    list_filter = ('sales_type',)

class SalespeopleAdmin(admin.ModelAdmin):
    list_display = ('salesperson_id', 'salesperson_name', 'store_id')

class SalesQuestionnairesAdmin(admin.ModelAdmin):
    list_display = ('sales_record', 'sales_process_score', 'warranty_process_score')

class ExperienceQuestionnairesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'usage_id', 'fill_time', 'willingness_to_use_again', 'massage_chair_mode_satisfaction')

class ExperienceReservationsAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'customer', 'store_id', 'reservation_time', 'salespeople')


admin.site.register(Customers, CustomersAdmin)
admin.site.register(MassageChairRecord, MassageChairRecordAdmin)
admin.site.register(PhysicalStores, PhysicalStoresAdmin)
admin.site.register(ReferralCodes, ReferralCodesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(OnlineStoreVisits, OnlineStoreVisitsAdmin)
admin.site.register(MassageChairs, MassageChairsAdmin)
admin.site.register(MassageChairModes, MassageChairModesAdmin)
admin.site.register(SalesRecords, SalesRecordsAdmin)
admin.site.register(Salespeople, SalespeopleAdmin)
admin.site.register(SalesQuestionnaires, SalesQuestionnairesAdmin)
admin.site.register(ExperienceQuestionnaires, ExperienceQuestionnairesAdmin)
admin.site.register(ExperienceReservations, ExperienceReservationsAdmin)