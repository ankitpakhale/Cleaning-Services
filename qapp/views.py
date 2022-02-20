from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Entry

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def query(request):
    # b = Blog(name = "ank", tagline = "this is just a demo tagline")
    # b.save()

  
    # doubted query
    entry = Entry.objects.get(pk=1)
    cheese_blog = Blog.objects.get(name="ank")
    entry.blog = cheese_blog
    entry.save()
    
    # joe = Author.objects.create(name = "Joe")
    # entry.authors.add(joe)
    
    # john = Author.objects.create(name = "John")
    
    return HttpResponse("working properly")
