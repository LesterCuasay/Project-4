from django.contrib import admin
from .models import BookingForm


class BookingFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'number_of_people',
        'date',
        'time',
    )


admin.site.register(BookingForm, BookingFormAdmin)
