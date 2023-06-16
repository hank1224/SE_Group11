from django.contrib import admin
from .models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_gender', 'phone_number', 'salesperson')
    search_fields = ('customer_name', 'phone_number')

class MassageChairRecordAdmin(admin.ModelAdmin):
    list_display = ('usage_id', 'customer', 'massage_chair', 'massage_chair_mode', 'start_time', 'payment', 'experience_questionnaires_fill')
    list_filter = ('payment', 'experience_questionnaires_fill')
    ordering = ('-start_time',)

class PhysicalStoresAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'branch_name')

class SalespeopleAdmin(admin.ModelAdmin):
    list_display = ('salesperson_id', 'salesperson_name', 'store_id')
    search_fields = ('salesperson_name',)

class ReferralCodesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'referral_code', 'used_referral_code')
    search_fields = ('customer__username__username',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_model', 'product_name', 'product_price', 'product_cost', 'product_warranty')
    list_filter = ('product_warranty',)

class CustomerWebViewsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'view_time')
    ordering = ('-view_time',)

class MassageChairsAdmin(admin.ModelAdmin):
    list_display = ('massage_chair_id', 'store_id', 'product_model')

class MassageChairModesAdmin(admin.ModelAdmin):
    list_display = ('massage_chair_mode_id', 'massage_chair_mode_name')

class SalesRecordsAdmin(admin.ModelAdmin):
    list_display = ('sales_record_id', 'customer', 'product', 'sales_time', 'sales_type', 'salesperson', 'store', 'sales_price')
    list_filter = ('sales_type',)
    search_fields = ('customer__username__username', 'product__product_name')

class SalesQuestionnairesAdmin(admin.ModelAdmin):
    list_display = ('sales_record', 'sales_process_score', 'warranty_process_score')

class ExperienceQuestionnairesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'usage_id', 'fill_time', 'willingness_to_use_again', 'massage_chair_mode_satisfaction')

class ExperienceReservationsAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'customer', 'reservation_time', 'store_id', 'salespeople')
    search_fields = ('customer__username__username',)

class CustomerADClicksAdmin(admin.ModelAdmin):
    list_display = ('customer', 'click_time')
    ordering = ('-click_time',)

admin.site.register(Customers, CustomersAdmin)
admin.site.register(MassageChairRecord, MassageChairRecordAdmin)
admin.site.register(PhysicalStores, PhysicalStoresAdmin)
admin.site.register(Salespeople, SalespeopleAdmin)
admin.site.register(ReferralCodes, ReferralCodesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(CustomerWebViews, CustomerWebViewsAdmin)
admin.site.register(MassageChairs, MassageChairsAdmin)
admin.site.register(MassageChairModes, MassageChairModesAdmin)
admin.site.register(SalesRecords, SalesRecordsAdmin)
admin.site.register(SalesQuestionnaires, SalesQuestionnairesAdmin)
admin.site.register(ExperienceQuestionnaires, ExperienceQuestionnairesAdmin)
admin.site.register(ExperienceReservations, ExperienceReservationsAdmin)
admin.site.register(CustomerADClicks, CustomerADClicksAdmin)