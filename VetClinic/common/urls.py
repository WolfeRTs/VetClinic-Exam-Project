from django.urls import path

from VetClinic.common.views import HomePageView, VetDashboardView, ContactsView, AboutUsView, DoctorsView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('doctors/', DoctorsView.as_view(), name='doctors'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('vet-dashboard/', VetDashboardView.as_view(), name='vet-dashboard'),
]