from django import forms
from .models import NutritionalInformation, Product


class NutritionalInformationForm(forms.ModelForm):
    class Meta:
        model = NutritionalInformation
        fields = ["name", "unit"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "nutritional_values", "status"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            # JSONField usa Textarea por defecto; añadimos placeholder útil
            "nutritional_values": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": '{\n  "Weight (g)": 159.0,\n  "Energetic value (Kcal)": 389.6,\n  "Proteins (g)": 5.4\n}'
            }),
        }
