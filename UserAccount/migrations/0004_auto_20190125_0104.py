# Generated by Django 2.1.5 on 2019-01-24 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0003_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
