import json

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from VetClinic.accounts.models import CustomUser
from VetClinic.permissions import is_vet
from VetClinic.pets.forms import PetAddForm, PetEditForm, PetDeleteForm, MedicalReportAddForm, MedicalReportEditForm, \
    MedicalReportDeleteForm
from VetClinic.pets.models import Pet, MedicalReport, PetStatus
from VetClinic.services.models import Service, Medicine


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
        return is_vet(self.request.user) or self.request.user == pet.owner


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
        pet = form.save(commit=False)
        if self.request.user.is_vet:
            owner_id = self.request.GET.get('owner_id')
            pet.owner = CustomUser.objects.get(pk=owner_id)
        else:
            pet.owner = self.request.user
        pet.save()

        status_data = form.get_pet_status_data()
        PetStatus.objects.create(pet=pet, **status_data)

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
        return is_vet(self.request.user) or self.request.user == pet.owner

    def form_valid(self, form):
        pet = form.save(commit=False)

        status_data = form.get_pet_status_data()
        for key, value in status_data.items():
            setattr(pet.status, key, value)
            pet.status.save()

        return super().form_valid(form)


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
        return is_vet(self.request.user) or self.request.user == pet.owner


class MedicalReportDashboard(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-dashboard.html'
    context_object_name = 'reports'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_id'] = self.kwargs['pet_id']
        return context

    def get_queryset(self):
        return MedicalReport.objects.filter(pet__id=self.kwargs['pet_id']).order_by('date_added')

    def test_func(self):
        pet = get_object_or_404(Pet, pk=self.kwargs['pet_id'])
        return is_vet(self.request.user) or self.request.user == pet.owner


class MedicalReportDetailsView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-details.html'
    context_object_name = 'report'
    pk_url_kwarg = 'report_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.object.services.all()
        context['medicines'] = self.object.medicines.all()
        return context

    def test_func(self):
        report = get_object_or_404(MedicalReport, pk=self.kwargs['report_id'])
        return self.request.user.has_perm('pets.view_medicalreport') or self.request.user == report.pet.owner


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

        services_data = self.request.POST.get('services', '[]')
        medicines_data = self.request.POST.get('medicines', '[]')

        if services_data:
            service_ids = json.loads(services_data)
        else:
            service_ids = []
        if medicines_data:
            medicine_ids = json.loads(medicines_data)
        else:
            medicine_ids = []

        services = Service.objects.filter(id__in=service_ids)
        medicines = Medicine.objects.filter(id__in=medicine_ids)

        for service in services:
            service.reports.add(form)

        for medicine in medicines:
            medicine.reports.add(form)


        return super().form_valid(form)

    def test_func(self):
        return self.request.user.has_perm('pets.add_medicalreport')


class MedicalReportEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalReport
    template_name = 'pets/medical-reports/report-edit.html'
    form_class = MedicalReportEditForm
    pk_url_kwarg = 'report_id'

    def get_success_url(self):
        return reverse_lazy(
            'report-details',
            kwargs={
                'pet_id': self.object.pet.pk,
                'report_id': self.object.pk
            }
        )

    def form_valid(self, form):
        report = form.save(commit=False)

        try:
            services_data = json.loads(self.request.POST.get('services', '[]'))
        except json.JSONDecodeError:
            services_data = []


        try:
            medicines_data = json.loads(self.request.POST.get('medicines', '[]'))
        except json.JSONDecodeError:
            medicines_data = []


        submitted_service_ids = {service['id'] for service in services_data}
        submitted_medicine_ids = {medicine['id'] for medicine in medicines_data}


        existing_service_ids = set(report.services.values_list('id', flat=True))
        existing_medicine_ids = set(report.medicines.values_list('id', flat=True))


        if submitted_service_ids != existing_service_ids:
            report.services.clear()
            for service_id in submitted_service_ids:
                report.services.add(service_id)


        if submitted_medicine_ids != existing_medicine_ids:
            report.medicines.clear()
            for medicine_id in submitted_medicine_ids:
                report.medicines.add(medicine_id)

        report.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['services'] = list(self.object.services.values('id', 'name'))
        context['medicines'] = list(self.object.medicines.values('id', 'name'))

        return context

    def test_func(self):
        return self.request.user.has_perm('pets.change_medicalreport')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.object.services.values_list('name', flat=True)
        context['medicines'] = self.object.medicines.values_list('name', flat=True)
        return context

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        return self.request.user.has_perm('pets.delete_medicalreport')