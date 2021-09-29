from django.urls import path
from .views import userSignUp, userLogin

urlpatterns = [
    path('', userSignUp, name='SIGNUP'),
    
    path('login/', userLogin, name='LOGIN'),

]
