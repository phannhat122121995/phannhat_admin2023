# Generated by Django 3.2.13 on 2022-05-30 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0018_imagss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Hiển Thị'), ('False', 'Ẩn')], default='True', max_length=15),
        ),
    ]
