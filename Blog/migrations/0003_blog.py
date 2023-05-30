# Generated by Django 3.2.13 on 2023-05-16 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0002_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('detail', models.TextField(blank=True)),
                ('images', models.ImageField(default='default.png', upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'Hiển Thị'), ('False', 'Ẩn')], default='True', max_length=15)),
                ('slug', models.SlugField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Blog.category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
