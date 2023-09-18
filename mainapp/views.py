from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from mainapp.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог товаров'
    }


class ProductDetailView(DetailView):
    model = Product

# class ProductListView(ListView):
#     model = Product
#     extra_context = {
#         'title': 'Карточка товара'
#     }

# def product(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Карточка товара'
#     }
#
#     return render(request, 'mainapp/product_detail.html', context)
