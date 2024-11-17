from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from VetClinic.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from VetClinic.accounts.models import Profile

UserModel = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('first_name', 'last_name', 'phone_number', 'city', 'country')

@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    model = UserModel
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = (ProfileInline, )

    list_display = ("username", "email", "is_staff", "is_vet",
                    "profile__first_name", "profile__last_name", "profile__phone_number")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_vet', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        if not request.user.is_superuser:
            return (
                (None, {'fields': ('username', 'email', 'password')}),
                ('Permissions', {'fields': ('is_vet',)}),
                ('Important dates', {'fields': ('last_login',)}),
            )

        return fieldsets