from django import forms
from django.db.models import fields
from .models import Product, item

class ProForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['CategoryName', 'ownerName', 'descriptionOfCategory', 'priceOfProduct', 'registration_date', 'rating']

    class Meta1:
        model = item
        fields = ['images' ,'title' ,'price', 'description']