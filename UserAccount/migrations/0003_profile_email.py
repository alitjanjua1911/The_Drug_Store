# Generated by Django 2.1.5 on 2019-01-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0002_auto_20190125_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
