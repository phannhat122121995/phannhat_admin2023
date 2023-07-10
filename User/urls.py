from django.urls import path

from User import views

urlpatterns = [
    path('', views.indexprofile, name='indexprofile'),
    path('cap-nhap/<int:id_user>/', views.update_pr, name='update_pr'),
    path('cap-nhap-moi/', views.create_profile, name='create_profile'),
    path('thong-tin-don-hang/', views.user_oder, name='user_oder_title'),
    path('thong-tin-chi-tiet/<int:id_oder>/', views.detail_oder, name='detail_oder'),
    path('cap-nhap-password/', views.change_password, name='change_password'),
    path('dang-xuat/', views.logout_func, name="logout_func"),
    path('chi-tiet-da-mua/<int:id>', views.detail_pro_bought, name='detail_pro_bought'),
]