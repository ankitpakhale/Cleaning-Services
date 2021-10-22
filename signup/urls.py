from django.urls import path
from .views import *

urlpatterns = [
    path('', userSignUp, name='SIGNUP'),
    
    path('login/', userLogin, name='LOGIN'),

    path('logout/', userLogOut, name='LOGOUT'),

    path('forgot/', forgot, name='FORGOT'),
    
    path('otpcheck/',otpCheck, name='OTPCHECK'),

    path('new_pass/',newPassword,name="NEWPASS"),
]