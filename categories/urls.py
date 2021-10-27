from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='MAIN'),    

    path('', product, name='PRODUCT'),
    
    path('cart/', add_to_cart, name='CART'),

    path('productView/<int:pk>', productView, name='PRODUCTVIEW'),
    path('productUpdate/<int:pk>', productUpdate, name='PRODUCTUPDATE'),
    path('productDelete/<int:pk>', productDelete, name='PRODUCTDELETE'),
]
