# Generated by Django 3.2.13 on 2022-06-10 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0022_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagss',
            old_name='title',
            new_name='title_im',
        ),
    ]
