# Generated by Django 3.2.13 on 2023-08-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0043_cource_video_titlevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cource_video',
            name='vimeo_link',
            field=models.URLField(blank=True),
        ),
    ]