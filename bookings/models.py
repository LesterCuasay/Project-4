from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# class BookingId(models.Model):
#     booking_id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False, null=False)
#     booking_id = models.ForeignKey(
#         'BookingId', on_delete=models.CASCADE, default=uuid.uuid4)

class BookingForm(models.Model):
    name = models.CharField(
        max_length=100, blank=True, verbose_name='Name', null=True)
    email = models.EmailField(
        default='example@example.com', verbose_name='Email')
    phone_number = models.CharField(
        default='07', verbose_name='Phone Number', max_length=11
    )
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
