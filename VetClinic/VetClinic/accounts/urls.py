from django.urls import path, include

from VetClinic.accounts.views import CustomUserLoginView, CustomUserLogoutView, CustomUserRegisterView, \
    ProfileDetailsView, ProfileEditView, CustomUserDeleteView

urlpatterns = [
    path('register/', CustomUserRegisterView.as_view(), name='register'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', CustomUserDeleteView.as_view(), name='profile-delete'),
    ]))
]