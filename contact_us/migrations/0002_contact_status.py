# Generated by Django 2.1.5 on 2019-01-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
