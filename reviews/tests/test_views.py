from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from reviews.models import BookingReview


class BookingReviewViewTest(TestCase):
    """
    Sets up a test use, test admin, and a reviewform
    so I can test the views using these parameters
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
            )
        self.admin = User.objects.create_superuser(
            username="admin",
            password="adminpassword"
        )
        self.reviewform = BookingReview.objects.create(
            author=self.user,
            email="test@email.com",
            comment="The booking was good",
            service_rating=4,
            food_rating=3,
            overall_rating=4,
        )

    def test_post_review_view(self):
        """
        Logs in user to check if they can access the review form
        """
        self.client.login(
            username="testuser",
            password="testpassword"
        )

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='reviews/index.html')

    def test_view_all_draft_reviews(self):
        """
        Logs in admin to check if they can access view all draft reviews,
        also logs in a normal user to see if they can access the page
        """
        self.client.login(
            username="admin",
            password="adminpassword",
        )
        response = self.client.get(reverse('view_all_draft_reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='reviews/view_all_draft_reviews.html')

        self.client.login(
            username="testuser",
            password="testpassword"
        )
        response = self.client.get(reverse('view_all_draft_reviews'))
        self.assertRaises(PermissionDenied)
