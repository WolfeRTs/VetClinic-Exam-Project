from django.db import models
from django.utils.translation import gettext_lazy as _


class PetSexChoices(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')
