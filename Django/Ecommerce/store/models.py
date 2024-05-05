from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categegory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  

    def __str__(self):
        return self.name

