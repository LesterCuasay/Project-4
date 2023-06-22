from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BookingForm


class BookingViewTest(TestCase):
    """
    Sets up a test user, test admin and a bookingform
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
        self.booking = BookingForm.objects.create(
            user=self.user,
            date="2023-06-18",
            time="12:00",
            number_of_people=4
        )

    def test_book_table_view(self):
        """
        Logs in a test user and checks if they can access the booking form
        """
        self.client.login(
            username="testuser",
            password="testpassword"
        )
        response = self.client.get(reverse('book_table'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='bookings/bookings.html')

    def test_book_table_view_unauthorised(self):
        """
        If a user is not logged in, check to see if they are directed
        back to the login page.
        """
        response = self.client.get(reverse('book_table'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='account/login.html')

    def test_view_all_bookings_view(self):
        self.client.login(
            username="admin",
            password="adminpassword"
        )
        response = self.client.get(reverse('view_all_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='bookings/all-bookings.html')

