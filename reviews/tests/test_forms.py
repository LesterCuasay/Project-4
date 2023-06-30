from django.test import TestCase
from reviews.forms import BookingReviewForm


class BookingReviewFormTest(TestCase):

    def test_form_validation(self):
        """
        Tests if BookingReviewForm validates the provided form data correctly,
        the test creates a dictionary called "form_data"
        as a sample data for the form
        """
        form_data = {
            "author": "John",
            "email": "john@example.com",
            "comment": "Our experience was really good!",
            "service_rating": 4,
            "food_rating": 4,
            "overall_rating": 4,
        }

        form = BookingReviewForm(data=form_data)
        self.assertTrue(form.is_valid())
