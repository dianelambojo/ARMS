# Generated by Django 3.1.1 on 2020-11-18 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0004_auto_20201118_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 18, 20, 16, 32, 549538)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 18, 20, 16, 32, 546542)),
        ),
    ]