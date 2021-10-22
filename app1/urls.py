from django.urls import path
from .views import *
from signup.views import userLogin, userSignUp

urlpatterns = [
    path('', home, name='HOME'),
    path('about/', about, name='ABOUT'),
    path('services/', services, name='SERVICES'),
    path('contact/', contact, name='CONTACT'),
    path('faq/', faq, name='FAQ'),
    path('404/', error, name='ERROR'),
    path('team/', team, name='TEAM'),
    path('pricing/', pricing, name='PRICING'),
    path('testimonials/', testimonials, name='TESTIMONIALS'),
    path('gallery/', gallery, name='GALLERY'),
    path('blog/', blog, name='BLOG'),
    path('blogsingle/', blogSingle, name='BLOGSINGLE'),

    path('mainproduct/', mainProduct, name='MAINPRODUCT'),

    path('product/<int:pk>', product, name='PRODUCT'),
    path('productView/<int:pk>', productList, name='PRODUCTLIST'),
    path('productUpdate/<int:pk>', productUpdate, name='PRODUCTUPDATE'),
    path('productDelete/<int:pk>', productDelete, name='PRODUCTDELETE'),

    path('calculator/', calculator, name='CALCULATOR'),
    path('<int:id1>/', show, name='SHOW'),

    path('login/', userLogin, name='LOGIN'),
    path('signup/', userSignUp, name='SIGNUP'),

    path('index/', index),
    path('list/', list),
    path('datasubmit/', datasubmit),
]
