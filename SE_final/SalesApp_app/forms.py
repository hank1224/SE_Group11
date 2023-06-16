from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from DB_app.models import SalesRecords, Salespeople, PhysicalStores


class SalespeopleRegisterForm(UserCreationForm):
    salesperson_name = forms.CharField(max_length=255, required=True)
    store_id = forms.ModelChoiceField(queryset=PhysicalStores.objects.all(), required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'salesperson_name', 'store_id']

class SalesRecordsForm(forms.ModelForm):
    class Meta:
        model = SalesRecords
        fields = ['customer', 'product', 'sales_price']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
        }
    