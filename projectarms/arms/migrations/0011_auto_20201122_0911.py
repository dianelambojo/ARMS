# Generated by Django 3.1.1 on 2020-11-22 01:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0010_auto_20201121_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 22, 1, 11, 55, 269157, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 22, 1, 11, 55, 269157, tzinfo=utc)),
        ),
    ]
