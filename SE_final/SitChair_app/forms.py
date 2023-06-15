from django import forms
from DB_app.models import *

class MassageChairRecordForm(forms.ModelForm):
    customer = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    massage_chair_mode = forms.ModelChoiceField(queryset=MassageChairModes.objects.all())
    class Meta:
        model = MassageChairRecord
        fields = ['customer', 'massage_chair', 'massage_chair_mode', 'payment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['massage_chair_mode'].widget.choices = [(m.massage_chair_mode_id, m.massage_chair_mode_name) for m in MassageChairModes.objects.all()]
        if 'initial' in kwargs:
            initial = kwargs['initial']
            if 'customer' in initial and initial['customer']:
                self.fields['customer'].initial = initial['customer']
                self.fields['customer'].widget.attrs['value'] = initial['customer']