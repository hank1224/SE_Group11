from django import forms
from DB_app.models import *

class MassageChairRecordForm(forms.ModelForm):
    massage_chair_mode = forms.ModelChoiceField(queryset=MassageChairModes.objects.all())
    class Meta:
        model = MassageChairRecord
        fields = ['massage_chair', 'massage_chair_mode', 'payment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['massage_chair_mode'].widget.choices = [(m.massage_chair_mode_id, m.massage_chair_mode_name) for m in MassageChairModes.objects.all()]

class ExperienceQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = ExperienceQuestionnaires
        fields = ['willingness_to_use_again', 'massage_chair_mode_satisfaction']

class ExperienceReservationForm(forms.ModelForm):
    class Meta:
        model = ExperienceReservations
        fields = ['reservation_time', 'store_id']