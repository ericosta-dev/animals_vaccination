from django import forms
from .models import Specie,Animal

class SpecieForm(forms.ModelForm):
    class Meta:
        model = Specie
        exclude = ('id',)

class AnimalsFilter(forms.Form):
    name = forms.TextInput()
    specie = forms.ModelChoiceField(
        label='Espécie',
        queryset=Specie.objects.filter(active=True),
        required = False
    )

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        exclude = ('id','user')
        widgets = {
            'birthdate': forms.TextInput(attrs={'placeholder':'', 'class': 'date date-picker'}),
        }
