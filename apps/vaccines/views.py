from re import template
from django.views.generic import ListView,CreateView,UpdateView,View
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Vaccine
from .forms import VaccineForm,VaccineFilter
# Create your views here.
class VaccinesListView(View):
    template_name = 'vaccines_list.html'

    def get(self,request):
        ctx = {}
        filter = VaccineFilter()
        ctx['filter'] = filter
        ctx['vaccines'] = Vaccine.objects.filter(active=True)

        return render(request, self.template_name, ctx)

    def post(self,request):
        filter = VaccineFilter()
        ctx = {'filter':filter}

        vaccines = Vaccine.objects.filter(active=True)

        specie = request.POST.get('specie')
        if specie:
            vaccines = Vaccine.objects.filter(specie=specie,active=True)

        ctx['vaccines'] = vaccines
        return render(request, self.template_name, ctx)

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