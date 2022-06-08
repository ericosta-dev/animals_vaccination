from django import forms
from .models import Vaccine
from ..animals.models import Specie 

class VaccineForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Vaccine
        exclude = ('id',)

class VaccineFilter(forms.Form):
    specie = forms.ModelChoiceField(
        label='Espécie',
        queryset=Specie.objects.filter(active=True),
        required = False
    )
    widgets = {
        'specie': forms.Select(attrs={'class': 'form-control'})
    }