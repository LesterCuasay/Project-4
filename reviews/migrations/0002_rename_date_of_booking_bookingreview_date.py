# Generated by Django 3.2.19 on 2023-07-14 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingreview',
            old_name='date_of_booking',
            new_name='date',
        ),
    ]
