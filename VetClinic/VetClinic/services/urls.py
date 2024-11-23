from django.urls import path, include

from VetClinic.services.views import ServiceListCreateView, ServiceDetailView, MedicineListCreateView, \
    MedicineDetailView, ServiceCategoriesDashboardView, ServicesByCategoryAPIView

urlpatterns = [
    path('', ServiceCategoriesDashboardView.as_view(), name='services-dashboard'),
    path('api/services/', include([
        path('', ServiceListCreateView.as_view(), name='services-list'),
        path('<int:pk>/', ServiceDetailView.as_view(), name='service-details'),
        path('fragment/<int:category_id>/', ServicesByCategoryAPIView.as_view(), name='services-fragment'),
    ])),
    path('api/medicines/', include([
        path('', MedicineListCreateView.as_view(), name='medicines-list'),
        path('<int:pk>/', MedicineDetailView.as_view(), name='medicine-details'),
    ])),
]