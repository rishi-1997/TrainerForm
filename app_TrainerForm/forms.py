from django import forms
from .models import Trainer


class TrainerForms(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'