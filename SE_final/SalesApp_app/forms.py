from django import forms
from DB_app.models import Salespeople, SalesRecords, PhysicalStores

class PhysicalSalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecords
        fields = ['customer', 'product', 'sales_type', 'salesperson', 'store', 'sales_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salesperson'].queryset = Salespeople.objects.none()
        self.fields['store'].queryset = PhysicalStores.objects.none()

        if 'sales_type' in self.data:
            try:
                sales_type_id = int(self.data.get('sales_type'))
                self.fields['salesperson'].queryset = Salespeople.objects.filter(store_id=sales_type_id)
                self.fields['store'].queryset = PhysicalStores.objects.filter(store_id=sales_type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['salesperson'].queryset = self.instance.store.salespeople_set.order_by('salesperson_name')
            self.fields['store'].queryset = self.instance.salesperson.store_id