from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model() 


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название объявления',
        max_length=70
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='pics/'
    )

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        verbose_name='Название объявления',
        max_length=70
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='pics/'
    )
    description = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(
        Category,
        related_name='products')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class Favorited(models.Model):
    user = models.ForeignKey(
        User,
        related_name='favorited',
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )

    class Meta:
        UniqueConstraint(fields=['user', 'products'], name='unique_favorited')