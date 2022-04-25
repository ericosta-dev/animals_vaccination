from django import forms
from .models import Vaccine

class VaccineForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Vaccine
        exclude = ('id',)