from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput


# User registration - create
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]  # password2 field is confirmation of the password.


# Login a User
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
