from django.db import models

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
    customer_type   = models.IntegerField()
    processor       = models.CharField(max_length=10)
    hdd             = models.IntegerField()
    ram             = models.IntegerField()
    os              = models.CharField(max_length=20)
    sna1            = models.CharField(max_length=30)
    sna2            = models.CharField(max_length=30)
    sna3            = models.CharField(max_length=30)
    service_type    = models.IntegerField()
    price           = models.DecimalField(decimal_places=2, max_digits=20)