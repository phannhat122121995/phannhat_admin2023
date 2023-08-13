from django.urls import path

from Home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('san-pham/<slug:slug>/', views.detai_product, name='detai_product'),
    path('addcommentpr/<int:id>', views.addcommentpr, name='addcommentpr'),
    path('addmessager/', views.addmessager, name='addmessager'),
]