from django.contrib.auth.forms import UserCreationForm  # Built-in Sign Up form for new user
from django.contrib.auth.models import User
from django import forms


class SignupUserForm(UserCreationForm):
    """
    Uses widgets to use Bootstrap styles for built-in registration form.
    https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={  # use widget to change field styling
        'class': 'form-control',  # bootstrap form styling
    }))
    first_name = forms.CharField(max_length=16,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                 }))
    last_name = forms.CharField(max_length=32,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                }))

    class Meta:
        model = User
        # Fields will be displayed in this order:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        # Designate built-in fields:
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
