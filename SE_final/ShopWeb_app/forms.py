from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from DB_app.models import *

class CustomerRegistrationForm(UserCreationForm):
    customer_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    GENDER_CHOICES = [
        ('1', '男'),
        ('2', '女'),
        ('3', '其他'),
        ('4', '不願透漏'),
    ]
    customer_gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'customer_name', 'email', 'customer_gender', 'phone_number']

class CustomerEditProfileForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # 無法修改email，因為email是User的屬性，不是Customer的屬性，且下方model無法同時修改兩個model
    class Meta:
        model = Customers
        fields = ['customer_name', 'customer_gender', 'phone_number']

class ReferralCodeForm(forms.ModelForm):
    class Meta:
        model = ReferralCodes
        fields = ['referral_code', 'used_referral_code']
        labels = {
                    'referral_code': '您的推薦碼',
                    'used_referral_code': '請輸入欲使用推薦碼',
                }
    referral_code = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class ReferralCodeForm_unfillable(forms.ModelForm):
    class Meta:
        model = ReferralCodes
        fields = ['referral_code', 'used_referral_code']
        labels = {
                            'referral_code': '您的推薦碼',
                            'used_referral_code': '請輸入欲使用推薦碼',
                        }
    referral_code = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))   
    used_referral_code = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))   

class SalesProcessEQForm(forms.ModelForm):
    class Meta:
        model = SalesQuestionnaires
        fields = ['sales_process_score']
        labels = {'sales_process_score': '請給予本次購買過程的滿意度分數'}
        
    
class WarrantyProcessEQForm(forms.ModelForm):
    class Meta:
        model = SalesQuestionnaires
        fields = ['warranty_process_score']
        labels = {'warranty_process_score': '請給予後續服務和保固的滿意度分數'}



