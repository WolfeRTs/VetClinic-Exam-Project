from django import forms

from VetClinic.mixins import FormFieldsUpdateMixin
from VetClinic.pets.models import Pet, MedicalReport


class BasePetForm(forms.ModelForm):
    is_neutered = forms.BooleanField(
        required=False
    )
    is_vaccinated = forms.BooleanField(
        required=False
    )
    last_vaccinated_at = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    last_external_deworming = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    last_internal_deworming = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if instance and hasattr(instance, 'status'):
            pet_status = instance.status
            self.fields['is_neutered'].initial = pet_status.is_neutered
            self.fields['is_vaccinated'].initial = pet_status.is_vaccinated
            self.fields['last_vaccinated_at'].initial = pet_status.last_vaccinated_at
            self.fields['last_external_deworming'].initial = pet_status.last_external_deworming
            self.fields['last_internal_deworming'].initial = pet_status.last_internal_deworming

    def get_pet_status_data(self):
        return {
            'is_neutered': self.cleaned_data.get('is_neutered'),
            'is_vaccinated': self.cleaned_data.get('is_vaccinated'),
            'last_vaccinated_at': self.cleaned_data.get('last_vaccinated_at'),
            'last_external_deworming': self.cleaned_data.get('last_external_deworming'),
            'last_internal_deworming': self.cleaned_data.get('last_internal_deworming'),
        }

    class Meta:
        model = Pet
        fields = [
            'name', 'species', 'breed', 'sex', 'date_of_birth',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'},
            )
        }


class PetAddForm(BasePetForm, FormFieldsUpdateMixin):
    custom_keyword = 'pet_add'

class PetEditForm(BasePetForm, FormFieldsUpdateMixin):
    custom_keyword = 'pet_edit'


class PetDeleteForm(BasePetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True


class MedicalReportBaseForm(forms.ModelForm):

    class Meta:
        model = MedicalReport
        fields = ['title', 'description', 'instructions']


class MedicalReportAddForm(MedicalReportBaseForm, FormFieldsUpdateMixin):

    custom_keyword = 'report_add'


class MedicalReportEditForm(MedicalReportBaseForm):

    custom_keyword = 'report_edit'


class MedicalReportDeleteForm(MedicalReportBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
