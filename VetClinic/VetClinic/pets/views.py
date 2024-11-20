from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from VetClinic.pets.forms import PetAddForm, PetEditForm, PetDeleteForm, MedicalReportAddForm, MedicalReportEditForm, \
    MedicalReportDeleteForm
from VetClinic.pets.models import Pet, MedicalReport


class PetDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Pet
    template_name = 'pets/pet/pet-details.html'
    pk_url_kwarg = 'pet_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_report'] = self.object.medical_reports.all().order_by('-date_added').first()
        return context

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pet_id'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner


class PetAddView(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = 'pets/pet/pet-add.html'
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
    template_name = 'pets/pet/pet-edit.html'
    form_class = PetEditForm
    pk_url_kwarg = 'pet_id'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={'pet_id': self.object.pk}
        )

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pet_id'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner


class PetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet/pet-delete.html'
    form_class = PetDeleteForm
    pk_url_kwarg = 'pet_id'

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
        pet = get_object_or_404(Pet, pk=self.kwargs['pet_id'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner


class MedicalReportDashboard(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-dashboard.html'
    context_object_name = 'reports'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_id'] = self.kwargs['pet_id']
        return context

    def get_queryset(self):
        return MedicalReport.objects.filter(pet__id=self.kwargs['pet_id'])

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pet_id'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == pet.owner


class MedicalReportDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-details.html'
    context_object_name = 'report'
    pk_url_kwarg = 'report_id'

    def test_func(self):
        report = get_object_or_404(MedicalReport, pk=self.kwargs['report_id'])
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user == report.pet.owner


class MedicalReportAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-add.html'
    form_class = MedicalReportAddForm

    def get_success_url(self):
        return reverse_lazy(
            'report-dashboard',
            kwargs={'pet_id': self.kwargs['pet_id']}
        )

    def form_valid(self, form):
        form = form.save(commit=False)
        pet = get_object_or_404(Pet, pk=self.kwargs['pet_id'])
        form.pet = pet
        form.doctor = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.groups.filter(name='Veterinarian').exists()


class MedicalReportEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-edit.html'
    form_class = MedicalReportEditForm
    pk_url_kwarg = 'report_id'

    def get_success_url(self):
        return reverse_lazy(
            'report-details',
            kwargs={'report_id': self.object.pk}
        )

    def test_func(self):
        return self.request.user.groups.filter(name='Veterinarian').exists()


class MedicalReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-delete.html'
    form_class = MedicalReportDeleteForm
    pk_url_kwarg = 'report_id'

    def get_success_url(self):
        return reverse_lazy(
            'report-dashboard',
            kwargs={'pet_id': self.object.pet.pk}
        )

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        return self.request.user.groups.filter(name='Veterinarian').exists()