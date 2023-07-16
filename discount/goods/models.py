from django.db import models


# Create your models here.
class Products(models.Model):
    rating = models.IntegerField(verbose_name="Рейтинг")
    img = models.ImageField(upload_to="goods/images/", default=None, verbose_name="Изображение")
    title = models.CharField(max_length=180, default="Название товара", verbose_name="Название")
    description = models.CharField(max_length=280, verbose_name="Описание")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    company = models.CharField(max_length=50, default="Компания", verbose_name="Компания")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class Register(models.Model):  # noqa: DJ10,DJ11,E261
    name = models.CharField(max_length=180)
    password = models.CharField(max_length=280)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
