# Generated by Django 3.2.19 on 2023-07-01 13:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_alter_bookingform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='date',
            field=models.DateField(blank=True, help_text='Please select a day from today onwards', validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 1)), django.core.validators.MaxValueValidator(datetime.date(2023, 7, 31))]),
        ),
    ]
