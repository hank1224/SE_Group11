from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('create_test_data/', views.create_test_data , name='create_test_data'),
]