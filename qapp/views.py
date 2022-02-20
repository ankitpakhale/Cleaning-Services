from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def query(request):
    # b = Blog(name = "ank", tagline = "this is just a demo tagline")
    # b.save()
    
    
    return HttpResponse("working properly")
