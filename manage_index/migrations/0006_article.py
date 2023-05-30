# Generated by Django 3.2.13 on 2022-05-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]