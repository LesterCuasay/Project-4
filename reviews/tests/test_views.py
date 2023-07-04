from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core import mail
from reviews.models import BookingReview
from reviews.views import send_review_confirmation_email


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
        self.review = BookingReview.objects.create(
            author=self.user,
            date="2023-06-18",
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

    def test_view_publish_reviews(self):
        """
        Logs in admin to check if they can access publish reviews,
        also logs in a normal user to see if they can access the page
        """
        self.client.login(
            username="admin",
            password="adminpassword",
        )
        review_id = self.review.id
        publish_url = reverse('publish_reviews', args=[review_id])
        response = self.client.get(publish_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='reviews/publish_review.html')

        self.client.login(
            username="testuser",
            password="testpassword",
        )
        review_id = self.review.id
        publish_url = reverse('publish_reviews', args=[review_id])
        response = self.client.get(publish_url)
        self.assertRaises(PermissionDenied)

    def test_view_delete_reviews(self):
        """
        Logs in admin to check if they can access delete reviews,
        also logs in a normal user to see if they can access the page
        """
        self.client.login(
            username="admin",
            password="adminpassword",
        )
        review_id = self.review.id
        delete_url = reverse('delete_reviews', args=[review_id])
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='reviews/delete_review.html')

        self.client.login(
            username="testuser",
            password="testpassword",
        )
        review_id = self.review.id
        delete_url = reverse('delete_reviews', args=[review_id])
        response = self.client.get(delete_url)
        self.assertRaises(PermissionDenied)

    def test_post_review_post_view(self):
        """
        Test if a user can make a new review and checks the status of the
        booking is 0 which is draft, then when the review is published
        status will be 1 it also tests if the user will get
        a review confirmation email when the review is published
        """

        review_id = self.review.id

        response = self.client.get(review_id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='index')

        review = BookingReview.objects.get(id=review_id)
        self.assertEqual(review.status, 0)

        review.status = 1
        review.save()

        published_review = BookingReview.objects.get(id=review_id)
        self.assertEqual(published_review.status, 1)

        send_review_confirmation_email(review)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Review Published')
        self.assertEqual(mail.outbox[0].to, ['test@email.com'])
