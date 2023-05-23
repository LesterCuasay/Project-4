from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class BookingForm(models.Model):
    user = models.ForeignKey(
        User, null=True, default='', on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, blank=True, verbose_name='Name', null=True)
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(verbose_name='Phone Number', max_length=11)
    number_of_people = models.PositiveIntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)],
        verbose_name='Number of People'
    )
    date = models.DateField(verbose_name='Date')
    special_requirements = models.TextField(
        blank=True, verbose_name='Special Requirements')

    def __str__(self):
        return self.name
