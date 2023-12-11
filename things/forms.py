from django import forms
from .models import Things

class ThingForm(forms.ModelForm):
    class Meta:
        model = Things
        fields = ['type','title', 'description', 'cost', 'image']
