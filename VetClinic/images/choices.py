from django.db import models
from django.utils.translation import gettext_lazy as _


class ImageCategoryChoices(models.TextChoices):
    CAROUSEL = 'Carousel', _('Carousel')
    GALLERY = 'Gallery', _('Gallery')
    OTHER = 'Other', _('Other')
