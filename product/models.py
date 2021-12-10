from django.conf import settings
from django.db import models


class Product(models.Model):
    prod_name = models.CharField(max_length=255, default=True)
    prod_detail = models.TextField(max_length=255, default=True)
    weight = models.TextField(max_length=255, default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Review(models.Model):
        name = models.CharField(max_length=60, default=True)
        review_body = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)
        product = models.ForeignKey('Product', on_delete=models.CASCADE)



