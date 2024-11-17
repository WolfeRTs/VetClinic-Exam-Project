from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.utils.translation import gettext_lazy as _

from VetClinic.accounts.forms import CustomUserCreationForm, CustomUserLoginForm

UserModel = get_user_model()

class CustomUserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class CustomUserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/login.html'


class CustomUserLogoutView(LogoutView):
    pass


class CustomUserDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        account = self.get_object()
        account.delete()
        messages.success(self.request, _('Your account has been deleted'))
        return redirect(self.success_url)
