# Generated by Django 3.2.13 on 2022-06-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0021_auto_20220602_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]