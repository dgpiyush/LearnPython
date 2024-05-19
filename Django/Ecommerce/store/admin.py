from django.contrib import admin

from . import models as store_models




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'categegory']
    list_filter = ['categegory']
    search_fields = ['name']


admin.site.register(store_models.Product, ProductAdmin)

admin.site.register(store_models.Category)


admin.site.register(store_models.WhishList)



class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'state','country','pincode']
    autocomplete_fields = ['user']

admin.site.register(store_models.Address, AddressAdmin)
