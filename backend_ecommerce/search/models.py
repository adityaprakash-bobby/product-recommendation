from django.conf import settings
from django.db import models

from products.models import Product
User = settings.AUTH_USER_MODEL

class SavedSearches(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    product_viewed = models.ManyToManyField(Product, blank=True)