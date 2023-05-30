from django.urls import path

from Order import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-item-cart/<int:id>', views.addtocart, name='addtocart'),
]