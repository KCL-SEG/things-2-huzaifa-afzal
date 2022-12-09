"""Forms of the project."""

from .models import Thing
from django.core.validators import RegexValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea() , 'quantity': forms.NumberInput()}
