# Generated by Django 3.2.13 on 2022-05-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0009_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'Hiển Thị'), ('False', 'Ẩn')], max_length=10),
        ),
    ]
