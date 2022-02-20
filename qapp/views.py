from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Entry, Author

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def query(request):
    # b = Blog(name = "ank", tagline = "this is just a demo tagline")
    # b.save()

    # doubted query 1
    # joe = Author.objects.create(name = "Joe")
    # entry.authors.add(joe)
    
  
    # doubted query 2
    entry = Entry.objects.get(pk=1)
    cheese_blog = Blog.objects.get(name="ank")
    entry.blog = cheese_blog
    entry.save()
    
    # john = Author.objects.create(name = "John")
    # lucky = Author.objects.create(name="Lucky")
    # harry = Author.objects.create(name="harry")
    # ank = Author.objects.create(name="ank")
    # entry.authors.add(john, lucky, harry, ank) 
    # above line will add multiple Author in Author field in Entry model
    # Entry --> Author --> above line
    
    return HttpResponse("working properly")