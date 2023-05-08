from django.db import models


# Create your models here.
class Products(models.Model):
    url = models.URLField(blank=True)
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=280)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.IntegerField()
