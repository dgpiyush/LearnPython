from django.contrib import admin

from . import models as store_models




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'categegory']
    list_filter = ['categegory']
    search_fields = ['name']


admin.site.register(store_models.Product, ProductAdmin)

admin.site.register(store_models.Category)
