# Generated by Django 4.2 on 2024-03-05 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
