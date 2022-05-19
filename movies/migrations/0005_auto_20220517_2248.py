# Generated by Django 3.2 on 2022-05-17 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_genres_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres_ids',
        ),
        migrations.AddField(
            model_name='movie',
            name='adult',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.BooleanField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
