from django import forms
from .models import Vaccine,VaccineSettings

class VaccineForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Vaccine
        exclude = ('id',)

class VaccineSettingsForm(forms.ModelForm):
    class Meta:
        model = VaccineSettings
        exclude = ('id',)