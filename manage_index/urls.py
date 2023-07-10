from django.urls import path

from manage_index import views

urlpatterns = [
    path('', views.index_admin, name='indexadmin'),
    path('test/', views.test, name='test'),
    path('add/', views.addcategory, name='addcategory'),
    path('list-category/', views.index_category, name='index_category'),
    path('update-category/<int:id>', views.update_category, name='update_category'),
    path('delete-category/<int:id>', views.delete_category, name='delete_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-products/', views.add_products, name='add_products'),
    path('list-product/', views.index_product, name='index_product'),
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
    path('list-oder-user/', views.list_oder_user, name='list_oder_user'),
    path('update-oder-user/<int:id>', views.update_oder_user, name='update_oder_user'),
    path('list-comment/', views.list_comment, name='list_comment'),
    path('update-list-comment/<int:id>', views.update_list_comment, name='update_list_comment'),
    path('list-comment-blog/', views.list_comment_blog, name='list_comment_blog'),
    path('update-list-comment-blog/<int:id>', views.update_list_combl, name='update_list_combl'),
    path('add-videos/', views.addlistvideo, name="addlistvideo"),
    path('list-vides-show/', views.listvideoall, name="listvideoall"),
    path('update-videos/<int:id>', views.update_list_video, name="update_list_video"),
    path('delete-videos/<int:id>', views.delete_videos, name="delete_videos"),
    # path('register/', views.register, name='register'),
]

