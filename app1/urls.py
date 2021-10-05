from django.urls import path
from app1.views import *
from signup.views import userLogin, userSignUp

urlpatterns = [
    path('', home, name='HOME'),
    path('about/', about, name='ABOUT'),
    path('services/', services, name='SERVICES'),
    path('contact/', contact, name='CONTACT'),
    path('faq/', faq, name='FAQ'),
    path('error/', error, name='ERROR'),
    path('team/', team, name='TEAM'),
    path('pricing/', pricing, name='PRICING'),
    path('testimonials/', testimonials, name='TESTIMONIALS'),
    path('gallery/', gallery, name='GALLERY'),
    path('blog/', blog, name='BLOG'),

    path('login/', userLogin, name='LOGIN'),
    path('signup/', userSignUp, name='SIGNUP'),

    path('index/', index),
    path('list/', list),
    path('datasubmit/', datasubmit),
]
