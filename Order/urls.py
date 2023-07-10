from django.urls import path

from Order import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('updateid/', views.updateid, name='update_id_cart_pro'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('thanh-toan/', views.checkout, name='checkout'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
    path('item-count/', views.cart_item_count, name='cart_item_count'),
]