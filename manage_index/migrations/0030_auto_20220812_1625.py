# Generated by Django 3.2.13 on 2022-08-12 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0029_auto_20220812_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='first_name1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='last_name',
            new_name='last_name1',
        ),
    ]