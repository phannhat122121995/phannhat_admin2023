# Generated by Django 3.2.13 on 2023-07-05 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_commentblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentblog',
            name='rate',
        ),
    ]
