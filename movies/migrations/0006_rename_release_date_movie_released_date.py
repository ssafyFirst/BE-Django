# Generated by Django 3.2 on 2022-05-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20220518_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_date',
            new_name='released_date',
        ),
    ]
