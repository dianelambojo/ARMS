# Generated by Django 3.1.1 on 2020-12-13 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arms', '0010_auto_20201211_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author', to='arms.author'),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='arms.category'),
        ),
    ]