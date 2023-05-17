from django.shortcuts import render
from django.views import View
from .models import BookingForm
from .forms import BookingTableForm


def book_table(request):
    booking_form = BookingTableForm()

    if request.method == 'POST':
        booking_form = BookingTableForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()

    context = {'form': booking_form}

    return render(request, 'bookings/bookings.html', context)
