from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

import uuid


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/', null=True)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/', null=True)
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

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.address_line_1}"
    

class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.first_name
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart.user.first_name} - {self.product.name}"


class Order(models.Model):
    ORDER_STATUS =  [('Pending', 'Pending'),('Dispatched', 'Dispatched'),('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')]
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, default='Pending', choices=ORDER_STATUS)
    rzp_order_id = models.CharField(max_length=255, null=True, blank=True)
    rzp_payment_id = models.CharField(max_length=255, null=True, blank=True)
    rzp_signature_id = models.CharField(max_length=255, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.first_name
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order.user.first_name} - {self.product.name}"