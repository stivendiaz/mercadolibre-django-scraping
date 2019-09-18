from datetime import datetime

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    queried_at = models.DateTimeField(default=datetime.now)
    selling_number = models.CharField(max_length=40,default=0)
    shipment = models.CharField(max_length=40,default=0)
