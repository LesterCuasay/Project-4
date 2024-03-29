# Generated by Django 3.2.19 on 2023-07-14 12:04

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0011_alter_bookingform_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('number_of_people', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Number of People')),
                ('date', models.DateField(blank=True, help_text='Please select a day from today onwards', validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 14)), django.core.validators.MaxValueValidator(datetime.date(2023, 8, 13))])),
                ('time', models.TimeField(verbose_name='Time')),
                ('special_requirements', models.TextField(blank=True, verbose_name='Special Requirements')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BookingForm',
        ),
    ]
