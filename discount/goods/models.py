from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=280)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.IntegerField()


class Register(models.Model):
    name = models.CharField(max_length=180)
    password = models.CharField(max_length=280)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
