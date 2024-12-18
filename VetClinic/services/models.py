from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseService(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
        unique=True,
        error_messages={
            'unique': _("A service with that name already exists."),
        }
    )

    description = models.TextField(
        _('description'),
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ServiceCategory(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
        unique=True,
        error_messages={
            'unique': _("A category with that name already exists."),
        }
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Service categories')


class Service(BaseService):
    category = models.ForeignKey(
        verbose_name=_('category'),
        to=ServiceCategory,
        related_name='category_services',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

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
