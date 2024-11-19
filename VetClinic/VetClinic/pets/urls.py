from django.urls import path, include

from VetClinic.pets.views import PetDetailsView, PetAddView, PetEditView, PetDeleteView

urlpatterns = [
    path('add/', PetAddView.as_view(), name='pet_add'),
    path('<int:pk>/', include([
        path('', PetDetailsView.as_view(), name='pet-details'),
        path('edit/', PetEditView.as_view(), name='pet-edit'),
        path('delete/', PetDeleteView.as_view(), name='pet-delete'),
    ])),
]