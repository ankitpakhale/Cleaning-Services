from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='INDEX'),
    path('', views.common, name='INDEX'),
    # path('add/', views.addition, name='ADD'),
    # path('sub', views.subtraction, name='SUB'),
    # path('mul/', views.multiplication, name='MUL'),
    # path('div/', views.division, name='DIV')
]