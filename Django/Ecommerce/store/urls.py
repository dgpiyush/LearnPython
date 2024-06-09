

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
   
    path('category/<int:category_id>/', views.category, name='category'),

    # product detail page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # basic routes
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

    # path for dashboard

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/address/', views.address, name='address'),
    path('dashboard/address/edit/<int:address_id>/', views.address_edit, name='address_edit'),
    path('dashboard/address/delete/<int:address_id>/', views.address_delete, name='address_delete'),
    path('dashboard/address/create/', views.address_create, name='address_create'),

    path('dashboard/orders/', views.orders, name='my_orders'),

    path('my-address', views.my_address, name='my_address'),



    # cart
    path('cart', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart-item/<int:product_id>', views.update_cart_item, name='update_cart_item'),


    # checkout 
    path('checkout', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),

    # test payment url 
    path('test/', views.test, name='test'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
