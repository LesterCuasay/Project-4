from django.test import TestCase
from datetime import date, timedelta
from .forms import BookingTableForm
from .models import BookingForm


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

    def test_phone_number_input(self):
        """
        Test if the phone number input is being valided properly,
        valid_phone_number test for the correct max_length(11) and returns true
        invalid_phone_number is set less than the max_length which
        also returns true.
        """
        valid_phone_number = "12345678901"

        invalid_phone_number = "123456789"

        form_data = {
            "phone_number": valid_phone_number,
            "email": "john@example.com",
            "number_of_people": 5,
            "time": "12:00",
        }

        form = BookingTableForm(data=form_data)
        self.assertTrue(form.is_valid())

        invalid_form_data = {
            "phone_number": invalid_phone_number,
            "email": "john@example.com",
            "number_of_people": 5,
            "time": "12:00",
        }

        invalid_form = BookingTableForm(data=invalid_form_data)
        self.assertTrue(invalid_form.is_valid())

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
            "You can only book up to one month in advance, "
            "Please choose another date."
        )

    def test_clean_date_past_date(self):
        """
        Test if the clean_date function raises an error when date inputted
        is in the past, the form data is set to be in the past which
        throws the errror.
        """
        form_data = {
            "date": date.today() - timedelta(days=1),
            "time": "12:00",
        }

        form = BookingTableForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["date"][0],
            "You cannot book in the past, Please choose a date in the present."
        )

    def test_clean_time_existing_booking(self):
        """
        Test if the clean_time function raises an error when an existing
        booking already exists with the same date and time, existing_booking
        is created from the BookingForm class to save an instance of the model
        and form_data is then passed through with the same date and time
        which throws the error.
        """

        # Creates a booking with specific date and time
        existing_booking = BookingForm.objects.create(
            date=date.today(),
            time="12:00",
            number_of_people=4
        )

        # Same data as existing_booking
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
        form.is_valid()

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["time"][0],
            "The timeslot on this day is alreay booked, "
            "Please choose another timeslot."
        )

        existing_booking.delete()
