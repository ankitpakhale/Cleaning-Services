from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.index, name='INDEX'),

    path('',common, name='COMMON'),
    
    # path('add/', views.addition, name='ADD'),
    # path('sub', views.subtraction, name='SUB'),
    # path('mul/', views.multiplication, name='MUL'),
    # path('div/', views.division, name='DIV')
]