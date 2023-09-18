from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import ProductListView, ProductDetailView

app_name = MainappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product')
]
