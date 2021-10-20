from django.urls import path
from .views import *

urlpatterns = [
    path('', userSignUp, name='SIGNUP'),
    
    path('login/', userLogin, name='LOGIN'),

    path('forgot/', forgot, name='FORGOT'),

    path('conf/',confirm,name='CONF'),

]