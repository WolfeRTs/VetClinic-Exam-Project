from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from VetClinic.accounts.models import Profile

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = "__all__"



class CustomUserLoginForm(AuthenticationForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )