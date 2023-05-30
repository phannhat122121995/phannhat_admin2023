# Generated by Django 3.2.13 on 2022-05-10 08:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0014_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title', primary_key=True, serialize=False, unique=True),
        ),
    ]
