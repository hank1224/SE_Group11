from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.index),
    path('index/', views.index, name='SalesApp/index'),
    path('login/', views.login_view, name='SalesApp/login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='SalesApp/index'), name='SalesApp/logout'),
    path('register/', views.register, name='SalesApp/register'),
    path('sales_sell/', views.sales_sell, name='SalesApp/sales_sell'),
    path('actions/', views.actions, name='SalesApp/actions'),
    path('send_ad_email/<int:customer_id>/', views.send_ad_email, name='send_ad_email'),
    path('send_EQ_email/<int:sales_record_id>/', views.send_EQ_email, name='send_EQ_email'),
    path('customer_detail/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('sales_record', views.sales_record, name='SalesApp/sales_record'),
    path('reservations/', views.reservations, name='SalesApp/reservations'),
]