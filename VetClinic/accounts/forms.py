from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from VetClinic.accounts.models import Profile
from VetClinic.mixins import FormFieldsUpdateMixin

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm, FormFieldsUpdateMixin):
    email = forms.EmailField(
        required=True
    )

    custom_keyword = 'register'

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = "__all__"


class CustomUserLoginForm(AuthenticationForm, FormFieldsUpdateMixin):

    custom_keyword = 'login'


class ProfileEditForm(forms.ModelForm, FormFieldsUpdateMixin):
    class Meta:
        model = Profile
        exclude = ('user', )

    custom_keyword = 'profile_edit'