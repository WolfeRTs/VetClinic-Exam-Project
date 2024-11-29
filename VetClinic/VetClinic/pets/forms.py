from django import forms

from VetClinic.pets.models import Pet, MedicalReport


class BasePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'sex', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'},
            )
        }


class PetAddForm(BasePetForm):
    pass


class PetEditForm(BasePetForm):
    pass


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


class MedicalReportAddForm(MedicalReportBaseForm):
    pass


class MedicalReportEditForm(MedicalReportBaseForm):
    pass


class MedicalReportDeleteForm(MedicalReportBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
