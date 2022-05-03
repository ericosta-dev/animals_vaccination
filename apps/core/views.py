from django.shortcuts import render
from django.views.generic import ListView
from apps.application.forms import ApplicationForm,VaccineApplicationInlineForm
from apps.application.models import VaccineApplication,Application
from apps.animals.models import Animal


# Create your views here.
class DashboardView(ListView):
    template_name = 'home.html'
    model = Animal

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['application_form'] = ApplicationForm()
        ctx['vaccine_form'] = VaccineApplicationInlineForm(instance=Application(),
         initial=[{}],form_kwargs={})
        return ctx