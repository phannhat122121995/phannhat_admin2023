from django.contrib import admin

# Register your models here.
from Blog.models import Category, Blog

admin.site.register(Category)
admin.site.register(Blog)
