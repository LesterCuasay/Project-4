from django.test import TestCase
from datetime import date, timedelta
from .forms import BookingTableForm


class BookingTableFormTest(TestCase):

    def test_form_validation(self):
        """
        Test if BookingTableForm validates the provided form data correctly,
        the test creates a dictionary called "form_data"
        as a sample data for the form.
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

    def test_clean_date_future_date(self):
        """
        Test if the clean_date function raises an error when date is
        more than one month from date.today(), the form data is set to be
        more than one month which throws the error.
        """
        form_data = {
            "date": date.today() + timedelta(days=31),
            "time": "12:00",
        }

        form = BookingTableForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["date"][0],
            "You can only book up to one month in advance, Please choose another date."
        )

    