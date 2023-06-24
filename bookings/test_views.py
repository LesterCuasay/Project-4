from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
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
        back to the login page
        """
        response = self.client.get(reverse('book_table'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='account/login.html')

    def test_view_all_bookings_view(self):
        """
        Tests if the admin can access the view_all_bookings
        """
        self.client.login(
            username="admin",
            password="adminpassword"
        )
        response = self.client.get(reverse('view_all_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='bookings/all-bookings.html')

    def test_view_all_bookings_view_unauthorised(self):
        """
        Tests if a normal user can access the view_all_bookings,
        it should raise error 403
        """
        self.client.login(
            username="testuser",
            password="testpassword"
        )
        response = self.client.get(reverse('view_all_bookings'))
        self.assertRaises(PermissionDenied)

    def test_view_booking_view(self):
        """
        Logs in a test user and checks if they can access the my bookings page
        """
        self.client.login(
            username="testuser",
            password="testpassword"
        )
        response = self.client.get(reverse('view_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='bookings/my-bookings.html')

    def test_view_booking_view_unauthorised(self):
        """
        If a user is not logged in, check to see if they are directed
        back to the login page
        """
        response = self.client.get(reverse('view_booking'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='account/login.html')

    def test_update_booking_view(self):
        """
        Tests if a user can access the update booking page
        """
        self.client.login(
            username="testuser",
            password="testpassword"
        )
        booking_id = self.booking.id
        update_url = reverse('update_booking', args=[booking_id])
        response = self.client.get(update_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='bookings/update-booking.html')

    def test_update_booking_view_unauthorised(self):
        """
        Tests if a normal user can access the update booking page,
        they should be redirected to the login page
        """
        booking_id = self.booking.id
        update_url = reverse('update_booking', args=[booking_id])
        response = self.client.get(update_url)

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response='account/login')

    def test_update_booking_view_post(self):
        """
        Test if a user can update their existing booking,
        and are redirected back to the view bookings page
        """

        booking_id = self.booking.id
        update_url = reverse('update_booking', args=[booking_id])
        new_date = "2023-07-18"
        new_time = "12:30"

        response = self.client.post(
            update_url,
            {
                'date': new_date,
                'time': new_time
            })

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response='view_booking')

    def test_delete_booking_view(self):
        """
        Tests if a user can access the delete booking page
        """
        self.client.login(
            username="testuser",
            password="testpassword"
        )
        booking_id = self.booking.id
        delete_url = reverse('delete_booking', args=[booking_id])
        response = self.client.get(delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='bookings/delete-booking.html')

    def test_delete_booking_view_unauthorised(self):
        """
        Tests if a normal user can access the delete booking page,
        they should be redirected to the login page
        """
        booking_id = self.booking.id
        delete_url = reverse('delete_booking', args=[booking_id])
        response = self.client.get(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response='account/login')