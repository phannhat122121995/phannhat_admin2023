# Generated by Django 3.2.13 on 2023-07-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0039_video_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_list',
            name='pdffile',
            field=models.FileField(blank=True, upload_to='filepdf/'),
        ),
    ]
