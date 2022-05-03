from django.urls import path
from django.views.generic.base import TemplateView
from apps.core.views import DashboardView


urlpatterns = [
    path('', DashboardView.as_view(), name='home'),   
]