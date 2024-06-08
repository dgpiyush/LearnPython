from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Address, Category, Product, Cart, CartProduct
from django.shortcuts import redirect
from django.urls import reverse


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

   
    

    


   