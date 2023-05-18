from allauth.account.forms import LoginForm
from django import forms


class CustomLogInForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLogInForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Username'
            })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Password'
            })
