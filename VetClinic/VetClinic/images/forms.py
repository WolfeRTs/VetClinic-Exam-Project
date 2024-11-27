from django import forms

from VetClinic.images.models import Image


class BaseImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['date_uploaded']


class ImageAddForm(BaseImageForm):
    pass


class ImageEditForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image', 'date_uploaded']
