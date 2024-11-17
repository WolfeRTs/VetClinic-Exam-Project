from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.-]+$"
    message = _(
        "Enter a valid username using only uppercase and lowercase letters, "
        "numbers, and ./-/_ characters!"
    )