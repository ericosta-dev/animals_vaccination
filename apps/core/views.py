from django.shortcuts import render
from django.views.generic import ListView
from apps.application.forms import ApplicationForm,VaccineApplicationInlineForm
from apps.application.models import VaccineApplication,Application
from apps.animals.models import Animal
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class DashboardView(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    model = Animal

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # if self.user.is_authenticated
        ctx['application_form'] = ApplicationForm(usuario=self.request.user)
        ctx['vaccine_form'] = VaccineApplicationInlineForm(instance=Application(),
         initial=[{}],form_kwargs={})


        # applications = Application.objects.filter(user = self.request.user,active=True).values_list('id', flat=True)	
        # #applications = Application.objects.all()	

        # animals = applications.order_by('animal__name').distinct('animal__name').values_list('animal__id', flat=True)
        # vaccines = []
        # for animal in animals:
        #     vaccines.append(VaccineApplication.objects.filter(active=True,application__animal = animal))
        # # ctx['vaccine_applications'] = VaccineApplication.objects.filter(active=True,application__in = applications)

        # # print (vaccines)
        # ctx['vaccines'] = vaccines
        applications = Application.objects.filter(user = self.request.user,active=True).order_by('-add_date')[:10]
        ctx['applications'] = applications

        next_applications = VaccineApplication.objects.filter(application__user = self.request.user,
                                                                application__active=True,
                                                                notify_date__isnull=False,
                                                                ).order_by('-add_date')
        ctx['next_applications'] = next_applications


        return ctx