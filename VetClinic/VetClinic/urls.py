from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VetClinic.common.urls')),
    path('accounts/', include('VetClinic.accounts.urls')),
    path('pets/', include('VetClinic.pets.urls')),
    path('services/', include('VetClinic.services.urls')),
    path('images/', include('VetClinic.images.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
