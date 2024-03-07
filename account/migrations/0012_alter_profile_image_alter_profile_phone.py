# Generated by Django 4.2 on 2024-03-06 21:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_profile_birth_date_profile_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='account/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Phone must be start 010, 011, 012, 015 and all number contains 11 digits', regex='^01[0|1|2|5][0-9]{8}$')]),
        ),
    ]
