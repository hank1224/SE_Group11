from django import forms
from DB_app.models import *

class MassageChairRecordForm(forms.ModelForm):
    class Meta:
        model = MassageChairRecord
        fields = ['customer', 'massage_chair', 'massage_chair_mode', 'payment']