from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from VetClinic.pets.choices import PetSexChoices
from VetClinic.validators import CapitalFirstLetterValidator

UserModel = get_user_model()


class Pet(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
        validators=[
            CapitalFirstLetterValidator(),
        ],
    )

    species = models.CharField(
        _('species'),
        max_length=50,
    )

    breed = models.CharField(
        _('breed'),
        max_length=50,
        null=True,
        blank=True,
    )

    sex = models.CharField(
        _('sex'),
        max_length=10,
        choices=PetSexChoices.choices,
    )

    date_of_birth = models.DateField(
        _('date of birth'),
    )

    owner = models.ForeignKey(
        verbose_name=_('owner'),
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='owner_pets',
    )

    date_added = models.DateField(
        _('date added'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class PetStatus(models.Model):
    pet = models.OneToOneField(
        verbose_name=_('pet'),
        to=Pet,
        on_delete=models.CASCADE,
        related_name='status',
        primary_key=True,
    )

    is_neutered = models.BooleanField(
        _('neutered'),
        default=False,
    )

    is_vaccinated = models.BooleanField(
        _('vaccinated'),
        default=False,
    )

    last_vaccinated_at = models.DateTimeField(
        _('last vaccination date'),
        blank=True,
        null=True,
    )

    last_external_deworming = models.DateTimeField(
        _('last external deworming'),
        blank=True,
        null=True,
    )

    last_internal_deworming = models.DateTimeField(
        _('last internal deworming'),
        blank=True,
        null=True,
    )


class MedicalReport(models.Model):

    title = models.CharField(
        _('title'),
        max_length=100,
    )

    description = models.TextField(
        _('description'),
    )

    instructions = models.TextField(
        _('instructions'),
    )

    date_added = models.DateTimeField(
        _('date added'),
        auto_now_add=True,
    )

    date_updated = models.DateTimeField(
        _('date updated'),
        auto_now=True,
    )

    doctor = models.ForeignKey(
        verbose_name=_('doctor'),
        to=UserModel,
        on_delete=models.SET_NULL,
        related_name='medical_reports',
        null=True,
        blank=True,
    )

    doctor_name = models.CharField(
        _('doctor name'),
        max_length=100,
        null=True,
        blank=True,
    )

    pet = models.ForeignKey(
        verbose_name=_('pet'),
        to=Pet,
        on_delete=models.CASCADE,
        related_name='medical_reports',
    )

    def __str__(self):
        return self.title
