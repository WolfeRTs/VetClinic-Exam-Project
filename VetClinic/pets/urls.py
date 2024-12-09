from django.urls import path, include

from VetClinic.pets.views import PetDetailsView, PetAddView, PetEditView, PetDeleteView, MedicalReportAddView, \
    MedicalReportDetailsView, MedicalReportEditView, MedicalReportDeleteView, MedicalReportDashboard

urlpatterns = [
    path('add/', PetAddView.as_view(), name='pet_add'),
    path('<int:pet_id>/', include([
        path('', PetDetailsView.as_view(), name='pet-details'),
        path('edit/', PetEditView.as_view(), name='pet-edit'),
        path('delete/', PetDeleteView.as_view(), name='pet-delete'),
        path('reports/', include([
            path('', MedicalReportDashboard.as_view(), name='report-dashboard'),
            path('add/', MedicalReportAddView.as_view(), name='report-add' ),
            path('<int:report_id>/', include([
                path('', MedicalReportDetailsView.as_view(), name='report-details'),
                path('edit/', MedicalReportEditView.as_view(), name='report-edit'),
                path('delete/', MedicalReportDeleteView.as_view(), name='report-delete'),
            ])),
        ]))
    ])),
]