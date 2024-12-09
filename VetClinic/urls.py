from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

urlpatterns = i18n_patterns(
    path('', include('VetClinic.common.urls')),
    path('accounts/', include('VetClinic.accounts.urls')),
    path('pets/', include('VetClinic.pets.urls')),
    path('services/', include('VetClinic.services.urls')),
    path('images/', include('VetClinic.images.urls')),
    path('set-language/', include('django.conf.urls.i18n')),
)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/', include('VetClinic.api_urls')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
