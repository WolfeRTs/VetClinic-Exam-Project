from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from VetClinic.services.models import ServiceCategory, Service, Medicine


@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Medicine)
class MedicineTranslationOptions(TranslationOptions):
    fields = ('description',)
