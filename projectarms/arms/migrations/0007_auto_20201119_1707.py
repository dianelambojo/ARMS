# Generated by Django 3.1.1 on 2020-11-19 09:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0006_merge_20201119_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 19, 9, 7, 16, 216219, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 19, 9, 7, 16, 215219, tzinfo=utc)),
        ),
    ]