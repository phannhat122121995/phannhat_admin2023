from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.
from manage_index.models import Brands


class Category(models.Model):
    STATUS = (
        ('True', 'Hiển Thị'),
        ('False', 'Ẩn'),
    )
    id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL,blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='default.png', upload_to='images/Blog/')
    slug = AutoSlugField(null=True, unique=True, populate_from='title', default=None)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Blog(models.Model):
    STATUS = (
        ('True', 'Hiển Thị'),
        ('False', 'Ẩn'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.TextField(blank=True)
    keywords = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    images = models.ImageField(default='default.png', upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    slug = models.SlugField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    STATUS = (
        ('New', 'Mới'),
        ('True', 'Ẩn'),
        ('False', 'Hiện'),
    )
    Blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment