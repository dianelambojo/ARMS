# Generated by Django 3.1.1 on 2020-11-21 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0008_auto_20201121_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 21, 11, 28, 30, 343008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 21, 11, 28, 30, 340020, tzinfo=utc)),
        ),
    ]
