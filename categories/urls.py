from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='MAIN'),    
    path('product', product, name='PRODUCT'),
    
    path('addtocart/<int:d>', add_to_cart,name='CART'),

    path('mycart/', show_mycart,name='MYCART'),

    path('removecart/<int:d>',removecart,name='REMOVECART'),

    path('productView/<int:pk>', productView, name='PRODUCTVIEW'),
    path('productUpdate/<int:pk>', productUpdate, name='PRODUCTUPDATE'),
    path('productDelete/<int:pk>', productDelete, name='PRODUCTDELETE'),
]
