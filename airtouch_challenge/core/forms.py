from django import forms
from .models import NutritionalInformation


class NutritionalInformationForm(forms.ModelForm):
    class Meta:
        model = NutritionalInformation
        fields = ["name", "unit"]
