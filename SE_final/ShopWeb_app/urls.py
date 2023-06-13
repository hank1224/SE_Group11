from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.index),
    path('index/', views.index, name='ShopWeb/index'),
    path('login/', views.login_view, name='ShopWeb/login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='ShopWeb/index'), name='ShopWeb/logout'), 
    path('register/', views.register, name='ShopWeb/register'),
    path('buy_product/<int:product_id>/', views.buy_product, name='ShopWeb/buy_product'),
    path('order/', views.order, name='ShopWeb/order'),
    path('warranty/', views.warranty, name='ShopWeb/warranty'),
]