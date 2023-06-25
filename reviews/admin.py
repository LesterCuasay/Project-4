from django.contrib import admin
from .models import BookingReview


class BookingReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'created_at', 'overall_rating')


admin.site.register(BookingReview, BookingReviewAdmin)
