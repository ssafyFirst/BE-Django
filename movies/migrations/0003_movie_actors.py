# Generated by Django 3.2 on 2022-05-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_alter_actor_profile_path'),
        ('movies', '0002_auto_20220519_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='movies', to='actors.Actor'),
        ),
    ]
