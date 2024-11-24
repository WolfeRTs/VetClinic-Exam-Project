from django import forms

from VetClinic.services.models import Service, Medicine


class ServicesBaseForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['reports']


class ServiceAddForm(ServicesBaseForm):
    pass


class ServiceEditForm(ServicesBaseForm):
    pass


class ServiceDeleteForm(ServicesBaseForm):
    pass


class MedicineBaseForm(ServicesBaseForm):
    class Meta:
        model = Medicine
        exclude = ['reports']


class MedicineAddForm(MedicineBaseForm):
    pass


class MedicineEditForm(MedicineBaseForm):
    pass


class MedicineDeleteForm(MedicineBaseForm):
    pass
