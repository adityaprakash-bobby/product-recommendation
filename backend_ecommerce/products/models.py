import os
import random
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

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
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title