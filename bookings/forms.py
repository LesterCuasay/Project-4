from django import forms
from django.forms import fields
from .models import BookingForm


class BookingTableForm(forms.ModelForms):
    class Meta:
        model = BookingForm
        fields = '__all__'
