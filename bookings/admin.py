from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'number_of_people',
        'date',
        'time',
    )


admin.site.register(Booking, BookingAdmin)
