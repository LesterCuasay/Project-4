from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
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


def is_admin(user):
    return user.is_superuser


@user_passes_test
def view_all_bookings(request):
    """
    Allows the admin to view all the bookings made.
    """

    bookings = BookingForm.objects.all().order_by("-id")

    context = {
        "bookings": bookings,
    }

    return request(request, "bookings/all-bookings.html", context)


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

            messages.success(request, "Table updated successfully!")
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
        return redirect("view_booking")

    context = {
        "booking": booking,
    }

    return render(request, "bookings/delete-booking.html", context)


def send_booking_confirmation_email(booking):
    user = booking.user
    subject = "Booking Confirmation"
    message = (
        f"Dear {user.username}, your booking has been confirmed!\n"
        f"Here are your booking details as follows:\n"
        f"{booking.date.strftime('%d-%m-%Y')}\n"
        f"{booking.time}"
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
