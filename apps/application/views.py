from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .models import VaccineApplication
from apps.animals.models import Animal
from django.contrib.auth.models import User
from .forms import VaccineApplicationInlineForm,ApplicationForm


def VaccineApplicationAddView(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = User.objects.get(pk=request.user.id)
            application.save()
            form_vaccine = VaccineApplicationInlineForm(request.POST,instance = application)
            for form_vac in form_vaccine:
                if form_vac.is_valid():
                    form_vac.save()
            
            return redirect(reverse_lazy('home'))
        else:
            ctx = {
                'application_form' : form,
                'vaccine_form' : form_vaccine
            }
            return redirect(reverse_lazy('home'),ctx)