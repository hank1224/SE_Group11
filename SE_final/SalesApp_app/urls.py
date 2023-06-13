from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('', views.index),
    path('index/', views.index, name='Sales_App/index'),
]