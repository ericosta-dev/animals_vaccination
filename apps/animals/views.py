from django.views.generic import ListView,CreateView,UpdateView,View
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import SpecieForm,AnimalsFilter,AnimalForm
from .models import Specie,Animal
from django.contrib.auth.models import User


class SpeciesListView(ListView):
    model = Specie
    template_name = 'species_list.html'

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['species'] = Specie.objects.filter(active=True)
        return ctx

class SpeciesAddView(CreateView):
    model = Specie
    form_class = SpecieForm
    success_message = 'Especie adicionada com sucesso!'
    template_name = 'species_form.html'
    success_url = reverse_lazy('species-list')

class SpeciesUpdateView(UpdateView):
    model = Specie
    form_class = SpecieForm
    success_message = 'Especie Editada com sucesso!'
    template_name = 'species_form.html'
    success_url = reverse_lazy('species-list')
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
    
    def form_valid(self,form):
        specie_form = form.save()
        return redirect(self.success_url)

class AnimalsListView(View):
    template_name='animals_list.html'
    
    def get(self,request):
        ctx={}
        form = AnimalsFilter()
        ctx['form'] = form    
        ctx['animals'] = Animal.objects.filter(active=True,user=self.request.user)
        return render(request, self.template_name, ctx)

    def post(self,request):
        form = AnimalsFilter()
        ctx = {'form':form}

        animals = Animal.objects.filter(active=True,user=self.request.user)

        specie = request.POST.get('specie')
        if specie:
            animals = Animal.objects.filter(breed__specie=specie)
           
        ctx['animals'] = animals
        return render(request, self.template_name, ctx)

class AnimalsAddView(CreateView):
    model = Animal
    form_class = AnimalForm
    success_message = 'Animal adicionada com sucesso!'
    template_name = 'animals_form.html'
    success_url = reverse_lazy('animals-list')

    def form_valid(self,form):
        animal_form = form.save(commit=False)
        animal_form.user = User.objects.get(pk=self.request.user.id)
        animal_form.save()
        return redirect(self.success_url)


class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    success_message = 'Animal Editado com sucesso!'
    template_name = 'animals_form.html'
    success_url = reverse_lazy('animals-list')
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx

    def form_valid(self,form):
        animal_form = form.save()
        return redirect(self.success_url)