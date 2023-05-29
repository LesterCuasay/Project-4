from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import BookingForm
from .forms import BookingTableForm


def book_table(request):

    if request.method == 'POST':
        booking_form = BookingTableForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('index')

    else:
        booking_form = BookingTableForm()

    context = {
        'form': booking_form,
        }

    return render(request, 'bookings/bookings.html', context)


@login_required
def view_booking(request):
    bookings = BookingForm.objects.filter(user=request.user)

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/my-bookings.html', context)
