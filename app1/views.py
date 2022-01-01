from django.db.models.query_utils import Q
from app1.models import *

from signup.models import signUp

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from app1.forms import ProForm, inputForm, ProForm1, ProductForm

import smtplib
from email.message import EmailMessage

# Create your views here.

def home1(request):
    return HttpResponse("This is a Home Page")

# def home1(request):
#     return render(request,'home1.html')

# def home(request):
#     return render(request,'home.html')


def home(request):
    if 'email' in request.session:
        user1 = request.session['email']
        print(user1)
        per = signUp.objects.get(email = user1)
        print(per)
        # print("This is name"+per.name)
        log = 'LOGOUT'
        return render(request, 'home.html', {'per' : per, 'log' : log})        
    return redirect('LOGIN')


def about(request):
        return render(request,'about.html')

def services(request):
    if 'email' in request.session:
        return render(request,'services.html')
    return redirect('LOGIN')

def contact1(request):
    if request.POST:
        Name = request.POST['name']
        Email = request.POST['email']
        Phone = request.POST['phone']
        Message = request.POST['message']
        con = contactForm()
        con.name = Name
        con.email = Email
        con.phone = Phone
        con.message = Message
        con.save()

        # return HttpResponseRedirect('http://127.0.0.1:8000/app1/contact/')

        value = "Your response has been saved"
        return render(request, 'contact.html', {'value' : value})
    return render(request, 'contact.html')        


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(message)
        
        msg = EmailMessage()
        msg.set_content(f'''     
        Thank you for contacting with us.
        
        Name : {name}
        email: {email}
        phone: {phone}
        message: {message}
        ''')
        msg['Subject'] = 'Washla Cleaning Services'
        msg['From'] = 'akp3067@gmail.com'
        msg['To'] = 'ankitpakhale786@gmail.com'
        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(
            "akp3067@gmail.com", 
            "Nailson@0745"
        )
        
        server.send_message(msg)
        server.quit()
        messages.info(request, 'Message had been sent. Thank you for your notes')
        # return redirect('CONTACT')    
        value = "Your message has been sent successfully"
        return render(request, 'contact.html', {'value' : value})
    return render(request, 'contact.html')    
    

def faq(request):
    if 'email' in request.session:
        return render(request,'faq.html')
    return redirect('LOGIN')

def error(request):
    return render(request,'404-error-page.html')

def team(request):
    if 'email' in request.session:
        return render(request,'our-team.html')
    return redirect('LOGIN')

def pricing(request):
    if 'email' in request.session:
        return render(request,'pricing.html')
    return redirect('LOGIN')

def testimonials(request):
    if 'email' in request.session:
        return render(request,'testimonials.html')
    return redirect('LOGIN')

def gallery(request):
    if 'email' in request.session:
        return render(request,'masonry-gallery.html')
    return redirect('LOGIN')

def blog(request):
    if 'email' in request.session:
        return render(request,'blog-grid.html')
    return redirect('LOGIN')

def blogSingle(request):
    if 'email' in request.session:
        return render(request,'blog-single.html')
    return redirect('LOGIN')
    

def base(request):
    return render(request,'base.html')

def mainProduct(request):
    if 'email' in request.session:
        obj1 = mainItem.objects.all()
       
        # search module start
        s = request.GET.get('search')
        if s:
            q = mainItem.objects.filter(Q(title__icontains = s) | Q(description__icontains = s))
        else:
            q = mainItem.objects.all()
            # q = f"{s} is not found"
        # search module end

        a = ProductForm(request.POST)
        if a.is_valid():
            a.save()
            messages.success(request, 'Done')
        return render(request, 'mainProduct.html', {'mainProd': obj1, 's': q})
    return redirect('LOGIN')
    
# def product(request):
#     obj1 = item.objects.all()
#     a = ProForm1(request.POST)
#     if a.is_valid():
#         a.save()
#         messages.success(request, 'Done')
#     return render(request, 'product.html', {'allProduct': obj1})

def product(request, pk):
    prod= get_object_or_404(item, pk=pk)
    a = ProForm1(request.POST)
    if a.is_valid():
        a.save()
        messages.success(request, 'Done')
    return render(request, 'product.html', {'allProduct': prod})

# def product(request, pk):
#     prod= get_object_or_404(item, pk=pk)
#     return render(request, 'product.html', {'allProduct': prod})

def productList(request, pk):
    prod= get_object_or_404(item, pk=pk)
    return render(request, 'subProduct.html', {'object':prod})

def productUpdate(request, pk):
    prod= get_object_or_404(item, pk=pk)
    form = ProForm1(request.POST or None, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('PRODUCT')
    return render(request, 'editProduct.html', {'form':form})

def productDelete(request, pk):
    prod= get_object_or_404(item, pk=pk)   
    prod.delete() 
    return redirect('PRODUCT')

def calculator(request):
    form = inputForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        input1 = cd['inputA']
        input2 = cd['inputB']
        output1 = input1 + input2
        # output2 = input1 - input2        
        # output3 = input1 * input2
        # output4 = input1 / input2
        return HttpResponseRedirect(f"/app1/{output1}")
    else:
        form = inputForm()
    return render(request, 'calculator.html', {'form' : form})

def show(request,id1):
    return HttpResponse(f"The calculations are : {id1}")


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
