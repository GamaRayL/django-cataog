from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import product, index

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product')
]