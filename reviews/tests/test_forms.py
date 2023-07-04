from django.test import TestCase
from reviews.forms import BookingReviewForm
from django.contrib.auth.models import User


class BookingReviewFormTest(TestCase):

    def test_form_validation(self):
        """
        Tests if BookingReviewForm validates the provided form data correctly,
        the test creates a dictionary called "form_data"
        as a sample data for the form
        """
        form_data = {
            "date": "2023-06-18",
            "email": "john@example.com",
            "comment": "Our experience was really good!",
            "service_rating": 4,
            "food_rating": 4,
            "overall_rating": 4,
        }

        user = User.objects.create(
            username="John",
        )

        form = BookingReviewForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertNotIn('status', form.cleaned_data)

        review = form.save(commit=False)
        review.author = user
        review.save()
        self.assertEqual(review.status, 0)
