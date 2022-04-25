
from django.urls import path
from .views import VaccinesListView,VaccinesAddView,VaccinesUpdateView

urlpatterns = [
    path('vaccines-list/',VaccinesListView.as_view(),name='vaccines-list'),
    path('vaccines-add/',VaccinesAddView.as_view(),name='vaccines-add'),
    path('vaccines-edit/<int:pk>',VaccinesUpdateView.as_view(),name='vaccines-edit'),
]