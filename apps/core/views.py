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


        applications = Application.objects.filter(user = self.request.user,active=True).values_list('id', flat=True)	

        animals = applications.order_by('animal__name').distinct('animal__name').values_list('animal__id', flat=True)
        vaccines = []
        for animal in animals:
            vaccines.append(VaccineApplication.objects.filter(active=True,application__animal = animal))
        # ctx['vaccine_applications'] = VaccineApplication.objects.filter(active=True,application__in = applications)

        # print (vaccines)
        ctx['vaccines'] = vaccines

        return ctx