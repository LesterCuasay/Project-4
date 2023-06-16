from django.test import TestCase
from datetime import date
from .forms import BookingTableForm


class BookingTableFormTest(TestCase):

    def test_form_validation(self):
        """
         Test if BookingTableForm validated the provided form data correctly,
         the test creates a dictionary called "form_data" as a sample data for the form.
        """
        form_data = {
            "name": "John",
            "email": "john@example.com",
            "phone_number": "12345678901",
            "number_of_people": 5,
            "date": date.today(),
            "time": "12:00",
            "special_requirements": "None",
        }

        form = BookingTableForm(data=form_data)
        self.assertTrue(form.is_valid())
