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
    SALES_TYPE_CHOICES = [
        ('1', '線上'),
        ('2', '實體'),
    ]
    sales_type = forms.CharField(widget=forms.HiddenInput(), initial='2')
    salesperson = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Salespeople.objects.all(), required=False)

    class Meta:
        model = SalesRecords
        fields = ['customer', 'product', 'sales_price']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None and user.is_authenticated:
            try:
                salesperson = Salespeople.objects.get(user=user)
                self.fields['salesperson'].initial = salesperson
            except Salespeople.DoesNotExist:
                pass