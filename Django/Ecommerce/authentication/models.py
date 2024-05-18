from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class CustomUser(AbstractUser):
    token = models.CharField(max_length=100, null=True)

    def generate_token(self):  
        token = get_random_string(length=10, allowed_chars='1234567890')
        return token
    

    def __str__(self):
        return self.username



