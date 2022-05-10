from django import forms
from .models import Application,VaccineApplication

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ('id','active','user')


class VaccineApplicationForm(forms.ModelForm):
    class Meta:
        model = VaccineApplication
        exclude = ('id','active')
        widgets = {
            'manufacturing_date': DateInput(),
            'due_date': DateInput(),
            'notify_date': DateInput(),

        }


VaccineApplicationInlineForm = forms.inlineformset_factory(
    Application,
    VaccineApplication,
    VaccineApplicationForm,
    extra=1
)