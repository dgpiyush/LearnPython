### Django Custom User Model

Django provides a built-in User model which is perfect for most projects. However, there may be scenarios where you need to create a custom User model to fit your needs.

#### Why Use a Custom User Model?

1. **Additional Fields**: The built-in User model only has a limited number of fields. If you need to add additional fields to the user model, such as phone number, address, etc, you would need to create a custom User model.
2. **Custom Authentication Methods**: The built-in User model has a very basic authentication method. If you need to implement custom authentication methods, such as custom login views or custom authentication backends, you would need to create a custom User model.
3. **Custom Permissions**: The built-in User model only has a limited set of permissions. If you need to create custom permissions, such as permissions based on specific models or permissions based on specific fields, you would need to create a custom User model.

#### How to Create a Custom User Model?

To create a custom User model, you would need to create a new model and subclass the built-in AbstractUser model. Here is an example of how to create a custom User model with an additional phone number field:

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
```

### Update in Settings.py

```python
AUTH_USER_MODEL = 'myapp.CustomUser'
```

### Update in admin.py

```python
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')

    # add view
    def add_view(self, request, form_url='', extra_context=None):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().add_view(request, form_url, extra_context)
    
    # change view
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().change_view(request, object_id, form_url, extra_context)
    

    




admin.site.register(CustomUser)


```
