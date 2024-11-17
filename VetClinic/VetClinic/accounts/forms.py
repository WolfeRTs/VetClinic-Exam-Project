from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email',)



class CustomUserLoginForm(AuthenticationForm):
    pass