from django.urls import path, include
from VetClinic.services.views import (
    ServiceListCreateView, ServiceDetailView, ServicesByCategoryAPIView,
    MedicineListCreateView, MedicineDetailView,
)
from VetClinic.common.views import search_view

urlpatterns = [
    path('search/', search_view, name='search'),

    path('services/', include([
        path('', ServiceListCreateView.as_view(), name='services-list'),
        path('<int:pk>/', ServiceDetailView.as_view(), name='service-api-details'),
        path('fragment/<int:category_id>/', ServicesByCategoryAPIView.as_view(), name='services-fragment'),
    ])),

    path('medicines/', include([
        path('', MedicineListCreateView.as_view(), name='medicines-list'),
        path('<int:pk>/', MedicineDetailView.as_view(), name='medicine-api-details'),
    ])),
]
