from django import forms
from django.forms.widgets import *
from .models import BookingReview
from crispy_forms.helper import FormHelper


class BookingReviewForm(forms.ModelForm):

    class Meta:
        model = BookingReview
        fields = "__all__"
        exclude = ["author", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['date'].widget = forms.DateInput(attrs={
            'type': 'date'
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Email Address'
        })
        self.fields['comment'].widget = forms.Textarea(attrs={
            'placeholder': 'Add your review here',
            'maxlength': '350'
        })
        self.fields['service_rating'] = forms.IntegerField(
            widget=HiddenInput(),
            initial=0,
        )
        self.fields['food_rating'] = forms.IntegerField(
            widget=HiddenInput(),
            initial=0,
        )
        self.fields['overall_rating'] = forms.IntegerField(
            widget=HiddenInput(),
            initial=0,
        )
