from django import forms
from django.forms.widgets import *
from .models import BookingReview
from crispy_forms.helper import FormHelper


class BookingReviewForm(forms.ModelForm):
    class Meta:
        model = BookingReview
        fields = "__all__"
        exclude = ["author", "status",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
