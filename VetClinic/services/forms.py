from django import forms

from VetClinic.mixins import FormFieldsUpdateMixin
from VetClinic.services.models import Service, Medicine


class ServicesBaseForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['reports']


class ServiceAddForm(ServicesBaseForm, FormFieldsUpdateMixin):
    custom_keyword = 'service_add'


class ServiceEditForm(ServicesBaseForm, FormFieldsUpdateMixin):
    custom_keyword = 'service_edit'


class ServiceDeleteForm(ServicesBaseForm):
    pass


class MedicineBaseForm(ServicesBaseForm):
    class Meta:
        model = Medicine
        exclude = ['reports']


class MedicineAddForm(MedicineBaseForm, FormFieldsUpdateMixin):
    custom_keyword = 'medicine_add'


class MedicineEditForm(MedicineBaseForm, FormFieldsUpdateMixin):
    custom_keyword = 'medicine_edit'


class MedicineDeleteForm(MedicineBaseForm):
    pass
