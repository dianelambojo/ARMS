# Generated by Django 3.1.1 on 2020-11-28 13:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('book_author_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('book_category_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('book_category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('book_cover', models.ImageField(upload_to='media/')),
                ('book_file', models.FileField(upload_to='media/')),
                ('book_year', models.DateField(default=django.utils.timezone.now)),
                ('book_tags', models.CharField(max_length=100)),
                ('book_summary', models.CharField(max_length=100)),
                ('book_info', models.CharField(default='', max_length=100)),
                ('is_bookmarked', models.BooleanField()),
                ('is_downloaded', models.BooleanField()),
                ('is_read', models.BooleanField()),
                ('book_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arms.author')),
                ('book_category_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arms.category')),
            ],
            options={
                'db_table': 'Books',
            },
        ),
    ]
