from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm  # noqa
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


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Username'
            })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Email Address'
            })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Password'
            })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Confirm Password'
            })


class CustomResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Email Address'
            })


class CustomResetKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetKeyForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Password'
            })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': "max-width:300px",
            'placeholder': 'Confirm Password'
            })
