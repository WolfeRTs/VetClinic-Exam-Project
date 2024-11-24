from django.urls import path

from VetClinic.common.views import HomePageView, VetDashboardView, search_view

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('vet-dashboard/', VetDashboardView.as_view(), name='vet-dashboard'),
    path('api/search/', search_view, name='search'),
]