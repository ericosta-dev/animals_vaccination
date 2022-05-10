from django.urls import path
from django.views.generic.base import TemplateView
from apps.core.views import DashboardView
from apps.application.views import VaccineApplicationAddView


urlpatterns = [
    path('', DashboardView.as_view(), name='home'),  
    path('vaccine-application-add/', VaccineApplicationAddView, name='vaccine-application-add'),  

]