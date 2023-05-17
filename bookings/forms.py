from django import forms
from django.forms import fields, TextInput, EmailInput, DateInput, NumberInput, Textarea
from .models import BookingForm


class BookingTableForm(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = '__all__'
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
                'placeholder': 'Number of People'
            }),
            'date': DateInput(attrs={
                'class': "form-control",
                'style': "max-width: 300px",
                'placeholder': 'Date'
            }),
            'special_requirements': Textarea(attrs={
                'class': "form-control",
                'rows': "3",
                'style': "max-width: 300px",
                'placeholder': 'Special Requirements'
            }),
        }
