# Generated by Django 4.2.2 on 2023-06-12 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 12, 11, 15, 59, 799903, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='job',
            name='pay',
            field=models.CharField(),
        ),
    ]
