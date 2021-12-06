from django.conf import settings
from django.db import models


class Product(models.Model):
    prod_name = models.CharField(max_length=255, default=None)
    weight = models.TextField(max_length=255, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)


