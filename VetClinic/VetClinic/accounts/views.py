from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.utils.translation import gettext_lazy as _

from VetClinic.accounts.forms import CustomUserCreationForm, CustomUserLoginForm, ProfileEditForm
from VetClinic.accounts.models import Profile

UserModel = get_user_model()

class CustomUserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class CustomUserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/login.html'


class CustomUserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class CustomUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('register')

    def get_object(self, queryset=None):
        return self.request.user

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user == user

    def delete(self, request, *args, **kwargs):
        account = self.get_object()
        account.delete()
        return redirect(self.success_url)


class ProfileDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

    def test_func(self):
        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == user

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )

