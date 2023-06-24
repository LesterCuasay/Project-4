from django.test import TestCase
from django.contrib.auth.models import User
from home.forms import CustomLogInForm, CustomSignupForm, CustomResetForm, CustomResetKeyForm


class CustomFormsTest(TestCase):
    """
    Tests if CustomSignupForm is working as intended
    """
    def test_custom_signup_form(self):
        form = CustomSignupForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })

        self.assertTrue(form.is_valid())

    def test_custom_reset_form(self):
        """
        Tests if CustomResetForm is working as intended
        """
        form = CustomResetForm(data={
            'email': 'test@example.com',
        })

        self.assertTrue(form.is_valid())

    def test_custom_reset_key_form(self):
        """
        Tests if CustomResetKeyForm is working as intended
        """
        form = CustomResetKeyForm(data={
            'password1': 'newpassword1!',
            'password2': 'newpassword1!'
        })

        self.assertTrue(form.is_valid())