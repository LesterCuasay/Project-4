from django import forms
from django.forms.widgets import *
from .models import BookingReview
from crispy_forms.helper import FormHelper


class BookingReviewForm(forms.ModelForm):

    RATING_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]

    class Meta:
        model = BookingReview
        fields = "__all__"
        exclude = ["author", "status",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Email Address'
        })
        self.fields['comment'].widget = forms.Textarea(attrs={
            'placeholder': 'Add your review here'
        })
        self.fields['service_rating'].widget = forms.Select(
            choices=self.RATING_CHOICES,
        )
        self.fields['service_rating'].initial = "3"
        self.fields['food_rating'].widget = forms.Select(
            choices=self.RATING_CHOICES,
        )
        self.fields['food_rating'].initial = "3"
        self.fields['overall_rating'].widget = forms.Select(
            choices=self.RATING_CHOICES,
        )
        self.fields['overall_rating'].initial = "3"
