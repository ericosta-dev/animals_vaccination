from django.urls import path
from .views import SpeciesListView,SpeciesAddView,SpeciesUpdateView,AnimalsListView,AnimalsAddView,AnimalUpdateView



urlpatterns = [
    path('species-list/',SpeciesListView.as_view(),name='species-list'),
    path('species-add/',SpeciesAddView.as_view(),name='species-add'),
    path('species-edit/<int:pk>',SpeciesUpdateView.as_view(),name='species-edit'),
    path('animals-list/',AnimalsListView.as_view(),name='animals-list'),
    path('animals-add/',AnimalsAddView.as_view(),name='animals-add'),
    path('animals-edit/<int:pk>',AnimalUpdateView.as_view(),name='animals-edit'),

]