# Generated by Django 2.1.5 on 2019-01-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_contact_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='workingTime_end',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='workingTime_start',
            field=models.IntegerField(null=True),
        ),
    ]
