from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Entry, Author

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def query(request):
    # 1st query
    # b = Blog(name = "ank", tagline = "this is just a demo tagline")
    # b.save()

    # 2nd query  
    # doubted query 1
    # joe = Author.objects.create(name = "Joe")
    # entry.authors.add(joe)
    
  
    # 3rd query
    # doubted query 2
    entry = Entry.objects.get(pk=1)
    cheese_blog = Blog.objects.get(name="ank")
    entry.blog = cheese_blog
    entry.save()
    
    # 4th query
    # john = Author.objects.create(name = "John")
    # lucky = Author.objects.create(name="Lucky")
    # harry = Author.objects.create(name="harry")
    # ank = Author.objects.create(name="ank")
    # entry.authors.add(john, lucky, harry, ank) 
    # above line will add multiple Author in Author field in Entry model
    # Entry --> Author --> above line
    
    # 5th query
    # all_entries = Entry.objects.all()
    # print(all_entries)
    
    # 6th query
    year = Entry.objects.filter(pub_date__year = 2010)
    print("Year is ", year)
    # on the basis of year we have filtered out all the entries of year 2022
    
    # 7th query
    authorName = Entry.objects.filter(blog__name = 'ank')
    print("Author Name is ", authorName)
    # on the basis of year we have filtered out all the entries of blog that contains name = 'ank'
    
    # doubted query
    data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fermentum turpis lorem, et ullamcorper nisi ultricies sed. Integer id odio suscipit, tempor lectus vel, sollicitudin nunc. Vivamus non vulputate lorem, nec egestas lectus. Sed volutpat magna sit amet nunc pulvinar dignissim. Nulla malesuada tortor vitae tellus blandit, id tincidunt velit finibus. Donec mattis, nunc in scelerisque dictum, est mi pulvinar lorem, nec feugiat felis justo in sem. Duis aliquam, erat eu eleifend lacinia, augue ante rhoncus diam, laoreet commodo risus ante a ante. Ut vitae mauris sodales, ullamcorper nulla sed, auctor lectus. Sed rhoncus nunc odio. Integer vel dapibus risus."
    print(data)
    authorName.body_text = data
    authorName.save()
    
    
    # 8th query
    # auth = Author(name="demo8", email = "demo8th@gmail.com").save()
    # print("This is 8th numbered query ",auth)
    
    
    
    
    
    return HttpResponse("working properly")
