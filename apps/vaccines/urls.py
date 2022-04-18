
from django.urls import path
from .views import VaccinesListView,VaccinesAddView,VaccinesUpdateView,VaccinesSettingsListView,VaccinesSettingsAddView,VaccinesSettingsUpdateView

urlpatterns = [
    path('vaccines-list/',VaccinesListView.as_view(),name='vaccines-list'),
    path('vaccines-add/',VaccinesAddView.as_view(),name='vaccines-add'),
    path('vaccines-edit/<int:pk>',VaccinesUpdateView.as_view(),name='vaccines-edit'),
    path('vaccines-settings-list/',VaccinesSettingsListView.as_view(),name='vaccines-settings-list'),
    path('vaccines-settings-add/',VaccinesSettingsAddView.as_view(),name='vaccines-settings-add'),
    path('vaccines-settings-edit/<int:pk>',VaccinesSettingsUpdateView.as_view(),name='vaccines-settings-edit'),

]