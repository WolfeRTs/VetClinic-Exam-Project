from django import forms

from VetClinic.images.models import Image
from VetClinic.mixins import FormFieldsUpdateMixin


class ImageAddForm(forms.ModelForm, FormFieldsUpdateMixin):

    custom_keyword = 'image_add'

    class Meta:
        model = Image
        exclude = ['date_uploaded']


class ImageEditForm(forms.ModelForm, FormFieldsUpdateMixin):

    custom_keyword = 'image_edit'

    class Meta:
        model = Image
        exclude = ['image', 'date_uploaded']
