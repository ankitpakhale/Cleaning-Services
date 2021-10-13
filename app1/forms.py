from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = mainItem
        fields = ['images', 'title', 'description']

class ProForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['CategoryName', 'ownerName', 'descriptionOfCategory', 'priceOfProduct', 'registration_date', 'rating']


class ProForm1(forms.ModelForm):
    class Meta:
        model = item
        fields = ['images' ,'title' ,'price', 'description']

class inputForm(forms.ModelForm):
    class Meta:
        model = inputmodel
        fields = '__all__'
