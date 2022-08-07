from django import forms

from apps.animals.models import Animal
from .models import Application,VaccineApplication

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.ModelForm):
    animal = forms.ModelChoiceField(
        required=False, queryset = Animal.objects.filter(active=True) 
    )

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['animal'].queryset = self.fields['animal'].queryset.filter(user=usuario)

    class Meta:
        model = Application
        exclude = ('id','active','user')




class VaccineApplicationForm(forms.ModelForm):
    class Meta:
        model = VaccineApplication
        exclude = ('id','active','sent')
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