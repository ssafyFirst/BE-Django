# Generated by Django 3.2 on 2022-05-17 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220517_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='adult',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres_ids',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
    ]
