from django import forms
from .models import Product

class ProForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['CategoryName', 'ownerName', 'descriptionOfCategory', 'priceOfProduct', 'registration_date', 'rating']