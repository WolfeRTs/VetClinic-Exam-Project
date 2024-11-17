from django.urls import path

from VetClinic.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]