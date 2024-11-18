from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from VetClinic.images.choices import ImageCategoryChoices
from VetClinic.images.validators import FileSizeValidator


class Image(models.Model):
    image = models.ImageField(
        _('image'),
        upload_to='images',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
            FileSizeValidator(3),
        ],
    )

    date_uploaded = models.DateTimeField(
        _('date uploaded'),
        auto_now_add=True,
    )

    category = models.CharField(
        _('category'),
        max_length=50,
        choices=ImageCategoryChoices.choices,
        default=ImageCategoryChoices.OTHER,
    )