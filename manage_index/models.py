from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, ImageField, FileInput, SlugField, \
    EmailInput, PasswordInput
from django.urls import reverse
from django import forms
from django.utils.text import slugify


class Category(models.Model):
    STATUS = (
        ('True', 'Hiển Thị'),
        ('False', 'Ẩn'),
    )
    id = models.IntegerField(primary_key=True)
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL,blank=True, null=True)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(default='default.png', upload_to='images/')
    slug = AutoSlugField(null=True, unique=True, populate_from='title', default=None)
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

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


class Brands(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'Hiển Thị'),
        ('False', 'Ẩn'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    brands = models.ForeignKey(Brands, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    images = models.ImageField(default='default.png', upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    price = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    promotion = models.DecimalField(max_digits=15, decimal_places=0, null=True, default=0)
    amount = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255)
    video = models.FileField(upload_to='videos/', blank=True)
    pdf_file = models.FileField(upload_to='filepdf/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class video_list(models.Model):
    title = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    ordinal_numbers = models.IntegerField(blank=True)
    videos = models.FileField(upload_to='videos/', blank=True)
    pdffile = models.FileField(upload_to='filepdf/', blank=True)


class couse_title(models.Model):
    title = models.CharField(max_length=255, blank=True)
    ordinal_numbers = models.IntegerField(blank=True, default=1)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)


class cource_video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    cource = models.ForeignKey(couse_title, on_delete=models.SET_NULL, blank=True, null=True)
    ordinal_numbers = models.IntegerField(blank=True)
    titlevideo = models.CharField(max_length=255, blank=True)
    vimeo_link = models.URLField(blank=True)
    videos = models.FileField(upload_to='videos/', blank=True)
    pdffile = models.FileField(upload_to='filepdf/', blank=True)


class Imagss(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    # title_im = models.CharField(max_length=200, blank=True)
    image_s = models.ImageField(blank=True, upload_to='images/')

    # def __str__(self):
    #     return self.title_im


class ProductForm(ModelForm):
    class Meta:
        choices_list = Category.objects.all()
        choices_list1 = Brands.objects.all()
        STATUS = [
            ('True', 'hiển thị'),
            ('False', 'ẩn'),
        ]
        model = Product
        fields = ['category', 'brands', 'title', 'keywords', 'description', 'detail', 'images', 'status', 'price', 'promotion', 'amount', 'slug', 'video', 'pdf_file']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control','id': 'title', 'placeholder': 'Tiêu đề', 'onkeyup':'ChangeToSlug();'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords', 'required': False}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Mô tả'}),
            'detail': Textarea(attrs={'class': 'form-control', 'id': 'summernote'}),
            'images': FileInput(attrs={'class': 'form-control'}),
            'category': Select(choices=choices_list, attrs={'class': 'form-control'}),
            'brands': Select(choices=choices_list1, attrs={'class': 'form-control'}),
            'status': Select(choices=STATUS, attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control', 'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number',}),
            'promotion': NumberInput(attrs={'class': 'form-control', 'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number', }),
            'amount': NumberInput(attrs={'class': 'form-control', 'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number', }),
            'slug': TextInput(attrs={'class': 'form-control', 'id': 'slug', 'onchange': 'getvalue()'}),
            'video': FileInput(attrs={'class': 'form-control'}),
            'pdf_file': FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Tiêu đề bài viết',
            'description': 'Mô tả',
            'detail': 'Nội dung',
            'images': 'Hình ảnh',
            'category': 'Danh mục',
            'brands': 'Thương hiệu',
            'status': 'Trạng thái',
            'price': 'Giá sản phẩm',
            'promotion': 'Giá khuyễn mãi',
            'amount': 'Số lượng',
            'video': 'videos',
            'pdf_file': 'file pdf',
        }


class ImagssForm(ModelForm):
    class Meta:
        model = Imagss
        fields = ['product', 'image_s']
        widgets ={
            # 'title_im': TextInput(attrs={'class': 'form-control', 'placeholder': 'alt', 'required': False}),
            'image_s': FileInput(attrs={'class': 'form-control', 'multiple': True}),
        }
        labels = {}


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentPro(models.Model):
    STATUS = (
        ('New', 'Mới'),
        ('True', 'Hiện'),
        ('False', 'Ẩn'),
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10,choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class CommentCourse(models.Model):
    STATUS = (
        ('New', 'Mới'),
        ('True', 'Ẩn'),
        ('False', 'Hiện'),
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    rate = models.IntegerField(default=1)
    image = models.ImageField(blank=True, upload_to='images/')
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10,choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=150)
    country = models.CharField(blank=True, max_length=100)
    image = models.ImageField(blank=True, default='default.png', upload_to='images/users/')

    def __str__(self):
        return self.user.username
