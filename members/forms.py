from django.contrib.auth.forms import UserCreationForm  # Sign Up form for new user
from django.contrib.auth.models import User
from django import forms


class SignupUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=16)
    last_name = forms.CharField(max_length=32)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
