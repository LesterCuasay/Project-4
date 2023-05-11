from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class BookingForm(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    number_of_people = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    date = models.DateField()
    special_requirements = models.TextField(blank=True)
