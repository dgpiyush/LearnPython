from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categegory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  

    def __str__(self):
        return self.name


class WhishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = 'WhishLists'
        verbose_name = 'WhishList'
