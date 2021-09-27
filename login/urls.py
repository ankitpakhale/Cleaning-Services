from django.urls import path
from .views import userLogin, userLogin1
from app1.views import home

urlpatterns = [
    path('login/', userLogin, name='LOGIN'),
    path('', userLogin1, name='LOGIN1'),
    path('home/', home, name='HOME'),
    
]
