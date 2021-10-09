from django import forms
from .models import Product, item, inputmodel

class ProForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['CategoryName', 'ownerName', 'descriptionOfCategory', 'priceOfProduct', 'registration_date', 'rating']

    class Meta1:
        model = item
        fields = ['images' ,'title' ,'price', 'description']

class inputForm(forms.ModelForm):

    class Meta:
        model = inputmodel
        fields = '__all__'
