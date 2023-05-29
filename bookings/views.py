from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def view_booking(request, pk):
    booking = get_object_or_404(BookingForm, pk=pk)
    bookings = BookingForm.objects.filter(user=request.user)

    if request.user != booking.user:
        return render(request, 'home/index.html')

    context = {
        'booking': booking,
        'bookings': bookings,
    }

    return render(request, 'bookings/my-bookings.html', context)
