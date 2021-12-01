from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='MAIN'),    
    path('product', product, name='PRODUCT'),
    
    path('addtocart/<int:d>/<str:s1>',add_to_cart,name='CART'),

    path('mycart/', show_mycart,name='MYCART'),

    path('removecart/<int:d>',removecart,name='REMOVECART'),
    
    path('myorder/',cartorder,name='MYORDER'),
    
    path('pay/',payment,name='PAYMENT'),
    
    path('custOrders/', customerOrder,name='CUSTOMERORDER'),
    
    path('donateMoney/',donateMoney,name='DONATEMONEY'),

    path('productView/<int:pk>', productView, name='PRODUCTVIEW'),
    path('productUpdate/<int:pk>', productUpdate, name='PRODUCTUPDATE'),
    path('productDelete/<int:pk>', productDelete, name='PRODUCTDELETE'),
]
