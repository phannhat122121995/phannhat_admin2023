# Generated by Django 3.2.13 on 2022-05-28 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0017_auto_20220523_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_index.product')),
            ],
        ),
    ]
