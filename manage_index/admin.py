from django.contrib import admin

# Register your models here.
from manage_index.models import Category, Brands, Product, Imagss, CommentPro, UserProfile

admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Product)
admin.site.register(Imagss)
admin.site.register(CommentPro)
admin.site.register(UserProfile)