from django import forms
from django.forms import fields
from django.forms.widgets import *
from .models import BookingForm
from django.core.exceptions import ValidationError
from datetime import date, timedelta


class BookingTableForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Email'
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Phone Number'
            }),
            'number_of_people': NumberInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Number of People',
                'max': '10',
            }),
            'date': DateInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'type': 'date'
            }),
            'special_requirements': Textarea(attrs={
                'class': "form-control",
                'rows': "3",
                'style': "max-width: 300px",
                'placeholder': 'Special Requirements'
            }),
        }

    def clean_date(self):
        selected_date = self.cleaned_data.get('date')
        max_date = date.today() + timedelta(days=30)

        if selected_date and selected_date > max_date:
            error_message = "You can only book up to one month in advance, Please choose another date."
            raise ValidationError(error_message)

        if selected_date and selected_date < max_date:
            error_message = "You cannot book in the past, Please choose a date in the present."
            raise ValidationError(error_message)

        return selected_date