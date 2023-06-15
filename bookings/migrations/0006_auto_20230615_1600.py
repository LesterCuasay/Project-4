# Generated by Django 3.2.19 on 2023-06-15 16:00

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20230612_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingform',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='date',
            field=models.DateField(blank=True, help_text='Please select a day from today onwards', validators=[django.core.validators.MinValueValidator(datetime.date(2023, 6, 15)), django.core.validators.MaxValueValidator(datetime.date(2023, 7, 15))]),
        ),
    ]