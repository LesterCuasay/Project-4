from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import BookingForm
from .forms import BookingTableForm


def book_table(request):
    """
    Allows the user to book a table, If the request method is POST
    then the form will save to the database. If not they will be redirected
    back to the form.
    """
    if request.method == 'POST':
        booking_form = BookingTableForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('view_booking')

    else:
        booking_form = BookingTableForm()

    context = {
        'form': booking_form,
        }

    return render(request, 'bookings/bookings.html', context)


@login_required
def view_booking(request):
    """
    Only if the user is logged in they will be able
    to see the bookings they have made, In the order of the booking ID.
    """
    bookings = BookingForm.objects.filter(
        user=request.user).order_by('-id')

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/my-bookings.html', context)


def update_booking(request, booking_id):
    """
    This enables the user to update their booking if needed.
    """
    booking = get_object_or_404(BookingForm, id=booking_id)

    if request.method == 'POST':
        booking_form = BookingTableForm(request.POST, instance=booking)

        if booking_form.is_valid():
            booking_form.save()
            return redirect('view_booking')

    else:
        booking_form = BookingTableForm(instance=booking)

    context = {
        'form': booking_form,
    }

    return render(request, 'bookings/update-booking.html', context)


def delete_booking(request, booking_id):
    """
    This enables the user to delete their booking if it is no longer required.
    """
    booking = get_object_or_404(BookingForm, id=booking_id)

    if request.method == 'POST':
        booking.delete()
        return redirect('view_booking')

    context = {
        'booking': booking,
    }

    return render(request, 'bookings/delete-booking.html', context)