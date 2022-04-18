from re import template
from django.views.generic import ListView,CreateView,UpdateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Vaccine,VaccineSettings
from .forms import VaccineForm,VaccineSettingsForm
# Create your views here.
class VaccinesListView(ListView):
    model = Vaccine
    template_name = 'vaccines_list.html'

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['vaccines'] = Vaccine.objects.filter(active=True)
        return ctx


class VaccinesAddView(CreateView):
    model = Vaccine
    form_class = VaccineForm
    success_message = 'Vacina adicionada com sucesso!'
    template_name = 'vaccines_form.html'
    success_url = reverse_lazy('vaccines-list')

class VaccinesUpdateView(UpdateView):
    model = Vaccine
    form_class = VaccineForm
    success_message = 'Vacina Editada com sucesso!'
    template_name = 'vaccines_form.html'
    success_url = reverse_lazy('vaccines-list')
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
    
    def form_valid(self,form):
        specie_form = form.save()
        return redirect(self.success_url)


# Vacinnes 

class VaccinesSettingsListView(ListView):
    model = VaccineSettings
    template_name = 'vaccines_settings_list.html'

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['settings'] = VaccineSettings.objects.filter(active=True)
        return ctx

class VaccinesSettingsAddView(CreateView):
    model = VaccineSettings
    form_class = VaccineSettingsForm
    success_message = 'Configurção de vacina adicionada com sucesso!'
    template_name = 'vaccines_settings_form.html'
    success_url = reverse_lazy('vaccines-settings-list')

class VaccinesSettingsUpdateView(UpdateView):
    model = VaccineSettings
    form_class = VaccineSettingsForm
    success_message = 'Configurção de vacina Editada com sucesso!'
    template_name = 'vaccines_settings_form.html'
    success_url = reverse_lazy('vaccines-settings-list')
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
    
    def form_valid(self,form):
        vaccine_settings_form = form.save()
        return redirect(self.success_url)