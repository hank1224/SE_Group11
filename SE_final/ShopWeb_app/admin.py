from django.contrib import admin
from .models import *

class CustomerWebViewsAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product_id', 'view_time')
    ordering = ('-view_time',)
    search_fields = ('customer',)

admin.site.register(CustomerWebViews, CustomerWebViewsAdmin)

# Register your models here.
