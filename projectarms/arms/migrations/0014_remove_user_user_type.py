# Generated by Django 3.1.1 on 2020-11-24 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0013_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]