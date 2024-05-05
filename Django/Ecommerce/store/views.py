from django.shortcuts import render

from .models import Category, Product



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