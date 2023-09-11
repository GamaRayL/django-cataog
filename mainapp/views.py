from django.shortcuts import render

from mainapp.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог товаров'
    }

    return render(request, 'main/index.html', context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Карточка товара'
    }

    return render(request, 'main/product.html', context)