

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
   
    path('category/<int:category_id>/', views.category, name='category'),

    # basic routes
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

    # path for dashboard

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/address/', views.address, name='address'),
    path('dashboard/address/edit/<int:address_id>/', views.address_edit, name='address_edit'),
    path('dashboard/address/delete/<int:address_id>/', views.address_delete, name='address_delete'),
    path('dashboard/address/create/', views.address_create, name='address_create'),
]
