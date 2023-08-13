from django.db import models

# Create your models here.


class Messagers(models.Model):
    Fullname = models.CharField(max_length=255, blank=True)
    Email = models.CharField(max_length=255, blank=True)
    Phone = models.CharField(max_length=255, blank=True)
    Note = models.TextField(blank=True)