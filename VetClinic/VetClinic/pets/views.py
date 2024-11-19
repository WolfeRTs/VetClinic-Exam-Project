from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from VetClinic.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from VetClinic.pets.models import Pet


class PetDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Pet
    template_name = 'pets/pet-details.html'

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pk'])
        print(pet)
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner


class PetAddView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = 'pets/pet-add.html'
    form_class = PetAddForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.request.user.pk}
        )

    def form_valid(self, form):
        form = form.save(commit=False)
        form.owner = self.request.user
        form.save()
        return super().form_valid(form)


class PetEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pet
    template_name = 'pets/pet-edit.html'
    form_class = PetEditForm
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={'pk': self.object.pk}
        )

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pk'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner


class PetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet-delete.html'
    form_class = PetDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.request.user.pk}
        )

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pk'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner