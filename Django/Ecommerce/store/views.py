from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Address, Category, Order, OrderProduct, Product, Cart, CartProduct
from django.shortcuts import redirect
from django.urls import reverse
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.db.transaction import atomic

import json




razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



def test(request):
    
    currency = 'INR'
    amount = 200*100  # Rs. 200
 

    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler/'


    print(razorpay_order_id)

 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'store/test.html', context)


def about(request):
    return render(request, 'store/about.html')
def faq(request):
    return render(request, 'store/faq.html')


def index(request):
    category_queryset = Category.objects.all()
    context = {'categories':category_queryset}
    return render(request, 'store/index.html',context)


def category(request, category_id):
    products_queryset = Product.objects.filter(categegory=category_id)

    context ={
        'category_id':category_id,
        'products':products_queryset
    }
   
    return render(request, 'store/category.html',context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product_detail.html',{'product':product})


# dashboard views

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'store/dashboard/index.html')

@login_required(login_url='login')
def address(request):
    print(request.path)
    print(reverse('address'))

    address_queryset = Address.objects.filter(user=request.user)
    return render(request, 'store/dashboard/address.html',{'addresses':address_queryset})


@login_required(login_url='login')
def address_edit(request, address_id):

    address_queryset = Address.objects.get(id=address_id)


    if request.method == 'POST':
        address_queryset.address_line_1 = request.POST.get('address_line_1')
        address_queryset.address_line_2 = request.POST.get('address_line_2')
        address_queryset.city = request.POST.get('city')
        address_queryset.state = request.POST.get('state')
        address_queryset.country = request.POST.get('country')
        address_queryset.pincode = request.POST.get('pincode')
        address_queryset.mobile = request.POST.get('mobile')
        address_queryset.email = request.POST.get('email')
        address_queryset.save()
        return redirect('address')

    return render(request, 'store/dashboard/address_form.html',{'address':address_queryset})


@login_required(login_url='login')
def address_delete(request, address_id):

    address_queryset = Address.objects.get(id=address_id)

    address_queryset.delete()

    return redirect('address')


@login_required(login_url='login')
def address_create(request):

    


    if request.method == 'POST':
        address_queryset = Address(user=request.user)
        address_queryset.address_line_1 = request.POST.get('address_line_1')
        address_queryset.address_line_2 = request.POST.get('address_line_2')
        address_queryset.city = request.POST.get('city')
        address_queryset.state = request.POST.get('state')
        address_queryset.country = request.POST.get('country')
        address_queryset.pincode = request.POST.get('pincode')
        address_queryset.mobile = request.POST.get('mobile')
        address_queryset.email = request.POST.get('email')
        address_queryset.save()
        return redirect('address')

    return render(request, 'store/dashboard/address_form.html',{'address':None})

@login_required(login_url='login')
def my_address(request):

    address_queryset = Address.objects.filter(user=request.user)

    address = list(address_queryset)

    address = [ {
        'id':a.id,
        'address_line_1':a.address_line_1,
        'address_line_2':a.address_line_2,
        'city':a.city,
        'state':a.state,
        'country':a.country,
        'pincode':a.pincode,
        'mobile':a.mobile,
        'email':a.email
    } for a in address]

    return  HttpResponse(json.dumps(address))






@login_required(login_url='login')
def orders(request):

    order_queryset = Order.objects.filter(user=request.user)

    return render(request, 'store/dashboard/orders.html',{'orders':order_queryset})

@login_required(login_url='login')
def cart(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_products = CartProduct.objects.filter(cart=cart)

    return render(request, 'store/cart.html',{'cart_products':cart_products,'cart':cart})

@login_required(login_url='login')
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)

    product_in_cart_count = CartProduct.objects.filter(cart=cart, product=product).count()


    if(product_in_cart_count > 0):
        poduct_in_cart =  CartProduct.objects.get(cart=cart, product=product)
        poduct_in_cart.quantity += 1
        poduct_in_cart.save()
        return redirect('cart')

    CartProduct.objects.create(cart=cart,product=product, quantity=1)


    return redirect('cart')

@login_required(login_url='login')
def remove_from_cart(request, product_id):

    product = Product.objects.get(id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    CartProduct.objects.get(cart=cart, product=product).delete()

    return redirect('cart')

@login_required(login_url='login')
def update_cart_item(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_product = CartProduct.objects.get(cart=cart, product=product)

    increment_quantity = request.GET.get('inc',0)
    decrement_quantity = request.GET.get('dcr',0)


    if(increment_quantity):
        cart_product.quantity += 1
    if(decrement_quantity):
        if(cart_product.quantity <= 1):
            cart_product.delete()
            return redirect('cart')
            
        cart_product.quantity -= 1
    
    cart_product.save()

    return redirect('cart')

   
    

    


@login_required(login_url='login')
@atomic
def checkout(request):

    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    cart_products = CartProduct.objects.filter(cart=cart)
    cart_products_count = cart_products.count()
    cart_products_total = 0 

    for cart_product in cart_products:
        cart_products_total += cart_product.product.price * cart_product.quantity




    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        address = request.POST.get('address')
        postalcode = request.POST.get('postal_code')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email', '')


        order = Order.objects.create(
            user=user,
            name = f'{first_name} {last_name}',
            address = address,
            postal_code = postalcode,
            mobile = mobile,
            email = email,
            total = cart_products_total
        )


        for cart_product in cart_products:
            OrderProduct.objects.create(
                order = order,
                product = cart_product.product,
                price = cart_product.product.price,
                quantity = cart_product.quantity
            )
        

        # clear cart and cart products
        cart_products.delete()
        cart.delete()


        return redirect('/payment/?order_id={}'.format(order.id))
    

      
    context = {}

    context['cart']  = cart
    context['cart_products']  = cart_products
    context['cart_products_count']  = cart_products_count
    context['cart_products_total']  = cart_products_total

    return render(request, 'store/checkout.html',context)



def payment(request):
    
    order_id = request.GET.get('order_id')

    order = Order.objects.get(id=order_id)

    total_amount  = int(order.total*100)



    razorpay_order = razorpay_client.order.create(dict(amount=total_amount,
                                                       currency='INR',
                                                       payment_capture='0'))
    

    order.rzp_order_id = razorpay_order['id']
    order.save()
    

    context = {}
    context['razorpay_order_id'] = razorpay_order['id']
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = total_amount
    context['currency'] = 'INR'
    context['callback_url'] = '/paymenthandler/'




    return render(request, 'store/payment.html', context)
  
    


  







@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":

        # try:
            # get the required parameters from post request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')



        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        print(razorpay_order_id,'razorpay_order_id')

        # verify the payment signature.
        result = razorpay_client.utility.verify_payment_signature(
            params_dict)
        

        if result is not None:

            order = Order.objects.filter(rzp_order_id=razorpay_order_id).first()

            print(order,'order')

            amount = int(order.total*100)  # Rs. 200
            # try:

            # capture the payemt
            razorpay_client.payment.capture(payment_id, amount)


            order.is_paid = True
            order.rzp_order_id = razorpay_order_id
            order.rzp_payment_id = payment_id
            order.rzp_signature_id = signature
            order.save()

                # render success page on successful caputre of payment
            return render(request, 'store/paymentsuccess.html')
                # except:
 
                #     # if there is an error while capturing payment.
                #     return render(request, 'store/paymentfail.html')
        else:
 
            #     # if signature verification fails.
            return render(request, 'store/paymentfail.html')
        # except:
 
            # if we don't find the required parameters in POST data
            return HttpResponse('BadRequest')
    else:
       # if other than POST request is made.
        return HttpResponse('Invalid request')

        




   

   

    

