from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class BookingForm(models.Model):
    name = models.CharField(
        max_length=100, blank=True, verbose_name='Name', null=True)
    email = models.EmailField(
        default='example@example.com', verbose_name='Email')
    number_of_people = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)],
        verbose_name='Number of People'
    )
    date = models.DateField(verbose_name='Date')
    special_requirements = models.TextField(
        blank=True, verbose_name='Special Requirements')

    def __str__(self):
        return self.name
