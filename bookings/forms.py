from django import forms
from django.forms import fields
from django.forms.widgets import *
from .models import BookingForm
from django.core.exceptions import ValidationError
from datetime import date, timedelta


class BookingTableForm(forms.ModelForm):

    TIME_CHOICES = [
        ('12:00', '12:00 PM'),
        ('12:30', '12:30 PM'),
        ('13:00', '13:00 PM'),
        ('13:30', '13:30 PM'),
        ('14:00', '14:00 PM'),
        ('14:30', '14:30 PM'),
        ('15:00', '15:00 PM'),
        ('15:30', '15:30 PM'),
        ('16:00', '16:00 PM'),
        ('16:30', '16:30 PM'),
        ('17:00', '17:00 PM'),
    ]

    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={
            'class': "form-control",
            'style': "max-width: 300px",
            }))

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