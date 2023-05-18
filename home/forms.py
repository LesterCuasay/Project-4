from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import *


class LogInForm(UserCreationForm):
    class Meta:
        fields = '__all__'
        widgets = {
            'login': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Username'
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Password'
            }),
        }
