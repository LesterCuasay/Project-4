from django import forms
from .models import BookingReview


class BookingReviewForm(forms.ModelForm):
    class Meta:
        model = BookingReview
        fields = "__all__"
        exclude = ["author"]
