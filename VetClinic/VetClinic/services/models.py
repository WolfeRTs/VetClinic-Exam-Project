from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseService(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        _('description'),
    )

    class Meta:
        abstract = True


class Service(BaseService):
    reports = models.ManyToManyField(
        verbose_name=_('reports'),
        to='pets.MedicalReport',
        related_name='services',
    )


class Medicine(BaseService):
    dosages = models.TextField(
        _('dosages'),
    )

    reports = models.ManyToManyField(
        verbose_name=_('reports'),
        to='pets.MedicalReport',
        related_name='medicines',
    )