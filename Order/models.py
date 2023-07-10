from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from manage_index.models import Product


class ProductCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title


class Order(models.Model):
    STATUS = (
        ('Processing', 'Đang xử lý'),
        ('Pending_payment', 'Chờ thanh toán'),
        ('Completed', 'Đã hoàng thành'),
        ('On_hold', 'Tạm giữ'),
        ('Cancelled', 'Đã hủy'),
        ('Refunded', 'Đã hoàng lại tiền'),
        ('Failed', 'Đơn hàng thất bại'),
        ('Draft', 'Draft'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=15, editable=False)
    Name = models.CharField(blank=True, max_length=200)
    Phone = models.CharField(blank=True, max_length=200)
    Mail = models.CharField(blank=True, max_length=200)
    Address = models.CharField(blank=True, max_length=225)
    note = models.CharField(blank=True, max_length=150)
    status = models.CharField(max_length=15, choices=STATUS, default='Processing')
    total = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class ProductTotalInCart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)