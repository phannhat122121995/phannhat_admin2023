# Generated by Django 3.2.13 on 2022-06-10 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0024_alter_imagss_title_im'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagss',
            old_name='image',
            new_name='image_s',
        ),
    ]
