from django.db import models
from DB_app.models import Customers, Products

class CustomerWebViews(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    view_time = models.DateTimeField(auto_now_add=True)

# Create your models here.
