from django.urls import path

from manage_index import views

urlpatterns = [
    path('', views.index_admin, name='index'),
    path('test/', views.test, name='test'),
    path('add/', views.addcategory, name='addcategory'),
    path('list-category/', views.index_category, name='index_category'),
    path('update-category/<int:id>', views.update_category, name='update_category'),
    path('delete-category/<int:id>', views.delete_category, name='delete_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-products/', views.add_products, name='add_products'),
    path('list-product/', views.index_product, name='index_product'),
    path('update-product/<int:id>', views.update_product, name='update_product'),
    path('delete-product/<int:id>', views.delete_product, name='delete_product'),
    path('delete-image/<int:id>', views.delete_image, name='delete_image'),
    path('geturl/', views.geturl, name='geturl'),
    path('geturls/', views.geturls, name='geturls'),
    path('geturlp/', views.geturlp, name='geturlp'),
    path('geturlps/', views.geturlps, name='geturlps'),
    path('login/', views.login_user, name='login_user'),
    path('update-profile/', views.updateprofile, name='updateprofile'),
    # path('register/', views.register, name='register'),
]