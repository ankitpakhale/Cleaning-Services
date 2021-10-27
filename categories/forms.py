from django import forms
from .models import *

class ProForm1(forms.ModelForm):
    class Meta:
        model = item
        fields = ['images' ,'title' ,'price', 'description']
