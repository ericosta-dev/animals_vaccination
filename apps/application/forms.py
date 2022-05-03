from django import forms
from .models import Application,VaccineApplication


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ('id','user','active')


class VaccineApplicationForm(forms.ModelForm):
    class Meta:
        model = VaccineApplication
        exclude = ('id','active')


VaccineApplicationInlineForm = forms.inlineformset_factory(
    Application,
    VaccineApplication,
    VaccineApplicationForm,
    extra=1
)