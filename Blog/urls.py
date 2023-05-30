from django.urls import path

from Blog import views

urlpatterns = [
    path('home-blog/', views.home_blog, name='home-blog-category'),
    path('add/', views.home, name='add-blog-category'),
    path('update-category/<int:id>', views.blog_update_category, name='blog-update-category'),
    path('add-blog/', views.add_blog, name='add-blog-title'),
    path('delete-category/<int:id>', views.delete_category, name='blog_delete_category'),
    path('update-blog/<int:id>', views.blog_update, name='blog-update'),
    path('list-blog/', views.list_blog, name='list-blog-all'),
    path('delete-blog/<int:id>', views.delete_blog, name='blog_delete_blog'),
    path('geturl/', views.geturl, name='geturl_blog'),
    path('geturls/', views.geturls, name='geturls_blog'),
    path('geturlblog/', views.geturlblog, name='geturlblog'),
    path('geturlblogu/', views.geturlblogu, name='geturlblogu')
]