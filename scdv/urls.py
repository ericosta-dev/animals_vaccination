from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("accounts/", include("apps.accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path('animals/',include('apps.animals.urls')),
    path('vaccines/',include('apps.vaccines.urls')),
    path('',include('apps.core.urls')),
]
