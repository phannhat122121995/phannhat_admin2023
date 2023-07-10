from django.contrib import admin

# Register your models here.
from Blog.models import Category, Blog, CommentBlog

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(CommentBlog)
