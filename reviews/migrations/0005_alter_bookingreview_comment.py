# Generated by Django 3.2.19 on 2023-07-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_bookingreview_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingreview',
            name='comment',
            field=models.TextField(max_length=350),
        ),
    ]
