from django.test import TestCase
from django.contrib.auth.models import User
from home.forms import CustomLogInForm, CustomSignupForm, CustomResetForm, CustomResetKeyForm


class CustomFormsTest(TestCase):
    def test_custom_signup_form(self):
        form = CustomSignupForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })

        self.assertTrue(form.is_valid())

