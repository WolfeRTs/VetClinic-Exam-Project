from django import template
from django.utils.translation import gettext as _

register = template.Library()


@register.filter
def placeholder(field, text):
    field.field.widget.attrs['placeholder'] = _(text)
    return field
