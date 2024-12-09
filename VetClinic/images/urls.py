from django.urls import path, include

from VetClinic.images.views import GalleryView, ImageAddView, ImageDeleteView, ImageEditView, ImageDetailsView

urlpatterns = [
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('add/', ImageAddView.as_view(), name='image-add'),
    path('<int:pk>/', include([
        path('', ImageDetailsView.as_view(), name='image-details'),
        path('edit/', ImageEditView.as_view(), name='image-edit'),
        path('delete/', ImageDeleteView.as_view(), name='image-delete'),
    ])),
]