from django.shortcuts import render, redirect
from django.views import View, generic
from .models import BookingForm
from .forms import BookingTableForm


def book_table(request):
    booking_form = BookingTableForm()

    if request.method == "POST":
        booking_form = BookingTableForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            # Redirect or display a success message
            return redirect('index')

    else:
        booking_form = BookingTableForm()

    print(booking_form.errors)
    context = {'form': booking_form}
    return render(request, 'bookings/bookings.html', context)