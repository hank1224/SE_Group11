from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('login/', views.login_view, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'), 
    path('register/', views.register, name='register'), 
    path('buy_product/<int:product_id>/', views.buy_product, name='buy_product'),
]