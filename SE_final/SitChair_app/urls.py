from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views
from ShopWeb_app.views import register

urlpatterns = [ 
    path('', views.index),
    path('index/', views.index, name='SitChair/index'),
    path('login/', views.login_view, name='SitChair/login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='SitChair/index'), name='SitChair/logout'),
    path('register/', register, name='SitChair/register'),
    path('use_massage_chair/', views.use_massage_chair, name='SitChair/use_massage_chair'),

]