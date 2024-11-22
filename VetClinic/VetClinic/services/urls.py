from django.urls import path

from VetClinic.services.views import ServiceListCreateView, ServiceDetailView, MedicineListCreateView, \
    MedicineDetailView

urlpatterns = [
    path('api/services/', ServiceListCreateView.as_view(), name='service-list'),
    path('api/services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('api/medicines/', MedicineListCreateView.as_view(), name='medication-list'),
    path('api/medicines/<int:pk>/', MedicineDetailView.as_view(), name='medication-detail'),
]