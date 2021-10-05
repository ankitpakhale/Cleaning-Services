from app1.models import Product, item, xyz
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from app1.forms import ProForm

# Create your views here.

def home1(request):
    return HttpResponse("This is a Home Page")

# def home1(request):
#     return render(request,'home1.html')

# def home(request):
#     return render(request,'home.html')

def home(request):
    obj1 = item.objects.all()
    a = ProForm(request.POST)
    if a.is_valid():
        a.save()
        messages.success(request, 'Done')
    return render(request, 'home.html', {'data':a, 'all': obj1})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def error(request):
    return render(request,'404-error-page.html')

def team(request):
    return render(request,'our-team.html')

def pricing(request):
    return render(request,'pricing.html')

def testimonials(request):
    return render(request,'testimonials.html')

def gallery(request):
    return render(request,'masonry-gallery.html')

def blog(request):
    return render(request,'blog-grid.html')

# def login1(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)

        log = xyz()
        log.name = Name
        log.email = Email
        log.number = Number
        log.save()
        return redirect('HOME')
    return render(request, 'LOGIN1')

# def login(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)

        log = xyz()
        log.name = Name
        log.email = Email
        log.number = Number
        log.save()
        return redirect('HOME')
    return render(request, 'LOGIN')

def index(request):
    return render(request,'index.html')

def list(request):
    obj = Product.objects.all()
    return render(request, 'list.html', {'xyz':obj})

def datasubmit(request):
    obj1 = Product.objects.all()
    a = ProForm(request.POST)
    if a.is_valid():
        a.save()
        messages.success(request, 'Done')
        return HttpResponseRedirect('http://127.0.0.1:8000/app1/datasubmit/')
    return render(request, 'list1.html', {'data':a, 'all': obj1})

# def list2(request):
#     if request.POST:
#         Category_Name = request.POST['category']
#         print(Category_Name)

#         owner_Name = request.POST['owner']
#         print(owner_Name)

#         description_Of_Category = request.POST['description']
#         print(description_Of_Category)

#         price_Of_Product = request.POST['price']
#         print(price_Of_Product)

#         registration_date = request.POST['registration']
#         print(registration_date)

#         rating_ = request.POST['rating']
#         print(rating_)

#         pro = Product()
#         pro.CategoryName = Category_Name
#         pro.ownerName = owner_Name
#         pro.descriptionOfCategory = description_Of_Category
#         pro.priceOfProduct = price_Of_Product
#         pro.registration_date = registration_date
#         pro.rating = rating_

#         pro.save()
#     return render(request, 'list2.html')
