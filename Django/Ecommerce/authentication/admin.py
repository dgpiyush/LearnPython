from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser as MyUser
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField





class UserAdmin(UserAdmin):

    list_display = ["username","email"]
    list_filter = ['is_active','is_staff','is_superuser']
    search_fields = ['username','email']
    readonly_fields = ['last_login', 'date_joined']

    fieldsets = [
        (None, {"fields": ["username","email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ['is_active','is_staff','is_superuser','user_permissions']}),
        ("Groups", {"fields": ["groups"]}),
        ("Important dates", {"fields": ["last_login", "date_joined"]}),
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username","email", "first_name", "last_name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["username"]
    ordering = ["email"]
    


# Now register the new UserAdmin...
admin.site.register(MyUser,UserAdmin)



