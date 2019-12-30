from django.db import models

# Create Class with attributes as below
# in setting.py add path of this Class as:
# 'products.apps.ProductsConfig'
# Terminal => manage.py makemigrations
# Terminal => python3 manage.py migrate


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

