# Generated by Django 3.2 on 2022-05-23 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20220520_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='uprdated_at',
            new_name='updated_at',
        ),
    ]
