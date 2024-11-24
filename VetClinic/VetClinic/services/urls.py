from django.urls import path, include

from VetClinic.services.views import ServiceListCreateView, ServiceDetailView, MedicineListCreateView, \
    MedicineDetailView, ServiceCategoriesDashboardView, ServicesByCategoryAPIView, ServiceCreateView, ServiceEditView, \
    MedicineCreateView, MedicineEditView

urlpatterns = [
    path('', ServiceCategoriesDashboardView.as_view(), name='services-dashboard'),
    path('service/', include([
        path('add/', ServiceCreateView.as_view(), name='service-add'),
        path('<int:service_id>/', include([
            path('edit/', ServiceEditView.as_view(), name='service-edit'),
        ])),
    ])),
    path('medicine/', include([
        path('add/', MedicineCreateView.as_view(), name='medicine-add'),
        path('<int:medicine_id>/', include([
            path('edit/', MedicineEditView.as_view(), name='medicine-edit'),
        ]))
    ])),
    path('api/', include([
        path('services/', include([
            path('', ServiceListCreateView.as_view(), name='services-list'),
            path('<int:pk>/', ServiceDetailView.as_view(), name='service-api-details'),
            path('fragment/<int:category_id>/', ServicesByCategoryAPIView.as_view(), name='services-fragment'),
        ])),
        path('medicines/', include([
            path('', MedicineListCreateView.as_view(), name='medicines-list'),
            path('<int:pk>/', MedicineDetailView.as_view(), name='medicine-api-details'),
        ]))
    ])),
]