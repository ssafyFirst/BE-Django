# Generated by Django 3.2 on 2022-05-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres_ids',
            field=models.ManyToManyField(related_name='movie', to='movies.Genre'),
        ),
    ]