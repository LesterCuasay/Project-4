from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required  # noqa
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.views import View
from .models import BookingForm
from .forms import BookingTableForm
from datetime import datetime


@login_required
def book_table(request):
    """
    Allows the user to book a table, If the request method is POST
    then the form will save to the database. If not they will be redirected
    back to the form.
    """
    if request.method == "POST":
        booking_form = BookingTableForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()

            send_booking_confirmation_email(booking)

            messages.success(request, "Table booked successfully!")
            return redirect("view_booking")

        else:
            messages.error(request, "Error in the form, Please try again.")

    else:
        booking_form = BookingTableForm()

    context = {
        "form": booking_form,
    }

    return render(request, "bookings/bookings.html", context)


def view_all_bookings(request):
    """
    Allows the admin to view all the bookings made.
    """
    if not request.user.is_superuser:
        raise PermissionDenied

    bookings = BookingForm.objects.all().order_by("-id")

    context = {
        "bookings": bookings,
    }

    return render(request, "bookings/all-bookings.html", context)


def error_403(request, exception):
    return render(request, '403.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request, *args, **kwargs):
    return render(request, '500.html')


@login_required
def view_booking(request):
    """
    Only if the user is logged in they will be able
    to see the bookings they have made, In the order of the booking ID.
    """
    bookings = BookingForm.objects.filter(user=request.user).order_by("-id")

    context = {
        "bookings": bookings,
    }

    return render(request, "bookings/my-bookings.html", context)


@login_required
def update_booking(request, booking_id):
    """
    This enables the user to update their booking if needed.
    """
    booking = get_object_or_404(BookingForm, id=booking_id)

    if request.method == "POST":
        booking_form = BookingTableForm(request.POST, instance=booking)

        if booking_form.is_valid():
            booking_form.save()

            send_update_confirmation_email(booking)

            messages.success(request, "Booking updated successfully!")
            return redirect("view_booking")

        else:
            messages.error(request, "Error in the form, Please try again.")

    else:
        booking_form = BookingTableForm(instance=booking)

    context = {
        "form": booking_form,
    }

    return render(request, "bookings/update-booking.html", context)


@login_required
def delete_booking(request, booking_id):
    """
    This enables the user to delete their booking if it is no longer required.
    """
    booking = get_object_or_404(BookingForm, id=booking_id)

    if request.method == "POST":
        booking.delete()

        send_cancellation_confirmation_email(booking)

        messages.error(request, "Booking deleted successfully!")
        if request.user.is_superuser:
            return redirect("view_all_bookings")
        else:
            return redirect("view_booking")

    context = {
        "booking": booking,
    }

    return render(request, "bookings/delete-booking.html", context)


def send_booking_confirmation_email(booking):
    """
    When a booking is made, the user will recieve an email
    containing the username, date and time of the completed form.
    The email template sent will be the html version, but if
    it cannot be rendered it will render the txt file instead.
    """

    user = booking.user
    subject = "Booking Confirmation"
    text_template = "bookings/booking_confirmation_email.txt"
    html_template = "bookings/booking_confirmation_email.html"

    context = {
        'username': user.username,
        'date': booking.date.strftime('%d-%m-%Y'),
        'time': booking.time.strftime('%H:%M'),
    }

    text_content = render_to_string(text_template, context)
    html_content = render_to_string(html_template, context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[booking.email],
    )

    email.attach_alternative(html_content, 'text/html')

    email.send()


def send_update_confirmation_email(booking):
    """
    When a booking is updated, the user will recieve an email
    containing the username, date and time of the completed form.
    The email template sent will be the html version, but if
    it cannot be rendered it will render the txt file instead.
    """
    user = booking.user
    subject = "Booking Update Confirmation"
    text_template = "bookings/booking_updated_email.txt"
    html_template = "bookings/booking_updated_email.html"

    context = {
        'username': user.username,
        'date': booking.date.strftime('%d-%m-%Y'),
        'time': booking.time.strftime('%H:%M'),
    }

    text_content = render_to_string(text_template, context)
    html_content = render_to_string(html_template, context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[booking.email],
    )

    email.attach_alternative(html_content, 'text/html')

    email.send()


def send_cancellation_confirmation_email(booking):
    """
    When a booking is cancelled, the user will recieve an email
    containing the username, date and time of the completed form.
    The email template sent will be the html version, but if
    it cannot be rendered it will render the txt file instead.
    """
    user = booking.user
    subject = "Booking Cancellation Confirmation"
    text_template = "bookings/booking_cancellation_email.txt"
    html_template = "bookings/booking_cancellation_email.html"

    context = {
        'username': user.username,
        'date': booking.date.strftime('%d-%m-%Y'),
        'time': booking.time.strftime('%H:%M'),
    }

    text_content = render_to_string(text_template, context)
    html_content = render_to_string(html_template, context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[booking.email],
    )

    email.attach_alternative(html_content, 'text/html')

    email.send()
