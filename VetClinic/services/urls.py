from django.urls import path, include

from VetClinic.services.views import ServiceCategoriesDashboardView, ServiceCreateView, ServiceEditView, \
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

]