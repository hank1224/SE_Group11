from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views
from ShopWeb_app.views import login_view

urlpatterns = [ 
    path('', views.index),
    path('index/', views.index, name='SitChair/index'),
    path('login/', login_view, name='SitChair/login'), 

]