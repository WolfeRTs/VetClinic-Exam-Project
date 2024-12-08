from django.db import models
from django.utils.translation import gettext_lazy as _


class PetSexChoices(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')


class PetSpeciesChoices(models.TextChoices):
    DOG = 'dog', _('Dog')
    CAT = 'cat', _('Cat')
    RABBIT = 'rabbit', _('Rabbit')
    RODENT = 'rodent', _('Rodent')
    BIRD = 'bird', _('Bird')
    REPTILE = 'reptile', _('Reptile')
    OTHER = 'other', _('Other')
