from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FileSizeValidator:
    DEFAULT_MAX_SIZE = 3

    def __init__(self, max_size:int=DEFAULT_MAX_SIZE, message=None):
        self.max_size = max_size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = _(f"Max file size is {self.max_size} MB!")
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.max_size * 1024 * 1024:
            raise ValidationError(self.message)