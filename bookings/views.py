from django.shortcuts import render
from django.views import View


class Book(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bookings/bookings.html')