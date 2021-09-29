from django.urls import path
from .views import userSignUp, userLogin
from app1.views import home

urlpatterns = [
    path('', userSignUp, name='SIGNUP'),
    
    path('login/', userLogin, name='LOGIN'),

    path('home/', home, name='HOME'),

]
