from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VetClinic.common.urls')),
    path('accounts/', include('VetClinic.accounts.urls')),
    path('pets/', include('VetClinic.pets.urls')),
]
