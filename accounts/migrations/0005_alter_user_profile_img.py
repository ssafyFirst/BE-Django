<<<<<<< HEAD
# Generated by Django 3.2 on 2022-05-23 01:42
=======
# Generated by Django 3.2 on 2022-05-23 01:43
>>>>>>> 2f3f8358a8e20701d5f104e254afce10fac2d78f

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220522_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_img'),
        ),
    ]
