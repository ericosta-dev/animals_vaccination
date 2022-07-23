from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("accounts/", include("apps.accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path('animals/',include('apps.animals.urls')),
    path('vaccines/',include('apps.vaccines.urls')),
    path('',include('apps.core.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
