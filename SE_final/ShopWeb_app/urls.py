from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.index),
    path('index/', views.index, name='ShopWeb/index'),
    path('login/', views.login_view, name='ShopWeb/login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='ShopWeb/index'), name='ShopWeb/logout'), 
    path('register/', views.register, name='ShopWeb/register'),
    path('edit_profile/', views.edit_profile, name='ShopWeb/edit_profile'),
    path('product_detail/<int:product_id>/', views.product_detail, name='ShopWeb/product_detail'),
    path('buy_product/<int:product_id>/', views.buy_product, name='ShopWeb/buy_product'),
    path('order/', views.order, name='ShopWeb/order'),
    path('warranty/', views.warranty, name='ShopWeb/warranty'),
    path('referral_code', views.referral_code, name='ShopWeb/referral_code'),
    path('sales_process_EQ/<int:sales_record_id>/', views.sales_process_EQ, name='ShopWeb/sales_process_EQ'),
    path('warranty_process_EQ/<int:sales_record_id>', views.warranty_process_EQ, name='ShopWeb/warranty_process_EQ'),
]