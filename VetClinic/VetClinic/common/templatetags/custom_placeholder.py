from django import template
from django.utils.translation import gettext as _

register = template.Library()


@register.filter
def placeholder(field, text):
    translated_text = _(text)
    field.field.widget.attrs['placeholder'] = translated_text
    return field
