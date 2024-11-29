from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from VetClinic.accounts.managers import CustomUserManager
from VetClinic.accounts.validators import UsernameValidator
from VetClinic.validators import CapitalFirstLetterValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        validators=[
            MinLengthValidator(3, _("Username should be at least 3 characters long")),
            UsernameValidator(),
        ],
        help_text=_(
            "The username should consist of uppercase and lowercase letters, "
            "numbers, and ./-/_ characters only"
        ),
        error_messages={
            "unique": _("A user with that username already exists!"),
        }
    )

    email = models.EmailField(
        _('email'),
        max_length=150,
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
    )

    is_vet = models.BooleanField(
        _('veterinarian'),
        default=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name=_('user'),
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    first_name = models.CharField(
        _('first name'),
        max_length=50,
        validators=[
            MinLengthValidator(2, _("First name should be at least 2 characters long")),
            CapitalFirstLetterValidator(),
        ],
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        _('last name'),
        validators=[
            MinLengthValidator(2, _("Last name should be at least 2 characters long")),
            CapitalFirstLetterValidator(),
        ],
        max_length=50,
        blank=True,
        null=True,
    )

    country = models.CharField(
        _('country'),
        max_length=50,
        validators=[
            MinLengthValidator(3, _("Country should be at least 3 characters long")),
            CapitalFirstLetterValidator(),
        ],
        blank=True,
        null=True,
    )

    city = models.CharField(
        _('city'),
        max_length=50,
        validators=[
            MinLengthValidator(3, _("City should be at least 3 characters long")),
            CapitalFirstLetterValidator(),
        ],
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        _('phone number'),
        max_length=10,
        validators=[
            MinLengthValidator(10, _("Phone number should be exactly 10 characters long")),
            RegexValidator(r'^[\d]*$', _("Phone number should consist of digits only")),
        ],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username

    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return self.user.username