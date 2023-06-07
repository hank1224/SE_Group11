from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customers, MassageChairRecord, SalesRecords, SalesQuestionnaires, ExperienceQuestionnaires, ExperienceReservations, Products, PhysicalStores, Salespeople, ReferralCodes, MassageChairs, MassageChairModes

class CustomerRegistrationForm(UserCreationForm):
    customer_name = forms.CharField(max_length=255, required=True)
    GENDER_CHOICES = [
        ('1', '男'),
        ('2', '女'),
        ('3', '其他'),
        ('4', '不願透漏'),
    ]
    customer_gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'customer_name', 'customer_gender', 'phone_number']

class MassageChairRecordForm(forms.ModelForm):
    class Meta:
        model = MassageChairRecord
        fields = ['customer', 'massage_chair', 'massage_chair_mode', 'payment']

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

class SalesQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = SalesQuestionnaires
        fields = ['sales_process_score', 'warranty_process_score']

class ExperienceQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = ExperienceQuestionnaires
        fields = ['usage_id', 'willingness_to_use_again', 'massage_chair_mode_satisfaction']

class ExperienceReservationForm(forms.ModelForm):
    class Meta:
        model = ExperienceReservations
        fields = ['customer', 'reservation_time', 'store_id', 'Salespeople']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_model', 'product_name', 'product_price', 'product_cost', 'product_warranty']

class PhysicalStoreForm(forms.ModelForm):
    class Meta:
        model = PhysicalStores
        fields = ['branch_name']

class SalespersonForm(forms.ModelForm):
    class Meta:
        model = Salespeople
        fields = ['salesperson_name', 'store_id']

class ReferralCodeForm(forms.ModelForm):
    class Meta:
        model = ReferralCodes
        fields = ['customer', 'referral_code', 'uesd_referral_code']

class MassageChairForm(forms.ModelForm):
    class Meta:
        model = MassageChairs
        fields = ['store_id', 'product_model']

class MassageChairModeForm(forms.ModelForm):
    class Meta:
        model = MassageChairModes
        fields = ['massage_chair_mode_name']