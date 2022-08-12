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

def home(request):
    if 'email' in request.session:
        user1 = request.session['email']
        per = signUp.objects.get(email = user1)
        log = 'LOGOUT'
        return render(request, 'home.html', {'per' : per, 'log' : log})        
    return redirect('LOGIN')

def about(request):
    if 'email' in request.session:
        return render(request,'about.html')
    return redirect('LOGIN')

def services(request):
    if 'email' in request.session:
        return render(request,'services.html')
    return redirect('LOGIN')

def contact(request):
    if 'email' in request.session:
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
                "manage.py.flush@gmail.com", 
                "Nikhil@404"
            )
            
            server.send_message(msg)
            server.quit()
            messages.info(request, 'Message had been sent. Thank you for your notes')
            # return redirect('CONTACT')    
            value = "Your message has been sent successfully"
            return render(request, 'contact.html', {'value' : value})
        return render(request, 'contact.html')    
    return redirect('LOGIN')

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
    if 'email' in request.session:
        return render(request,'base.html')
    return redirect('LOGIN')

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
    if 'email' in request.session:
        prod= get_object_or_404(item, pk=pk)
        a = ProForm1(request.POST)
        if a.is_valid():
            a.save()
            messages.success(request, 'Done')
        return render(request, 'product.html', {'allProduct': prod})
    return redirect('LOGIN')

# def product(request, pk):
#     prod= get_object_or_404(item, pk=pk)
#     return render(request, 'product.html', {'allProduct': prod})

def productList(request, pk):
    if 'email' in request.session:
        prod= get_object_or_404(item, pk=pk)
        return render(request, 'subProduct.html', {'object':prod})
    return redirect('LOGIN')

def productUpdate(request, pk):
    if 'email' in request.session:
        prod= get_object_or_404(item, pk=pk)
        form = ProForm1(request.POST or None, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('PRODUCT')
        return render(request, 'editProduct.html', {'form':form})
    return redirect('LOGIN')

def productDelete(request, pk):
    if 'email' in request.session:
        prod= get_object_or_404(item, pk=pk)   
        prod.delete() 
        return redirect('PRODUCT')
    return redirect('LOGIN')

def list(request):
    if 'email' in request.session:
        obj = Product.objects.all()
        return render(request, 'list.html', {'xyz':obj})
    return redirect('LOGIN')

def datasubmit(request):
    if 'email' in request.session:
        obj1 = Product.objects.all()
        a = ProForm(request.POST)
        if a.is_valid():
            a.save()
            messages.success(request, 'Done')
            return HttpResponseRedirect('http://127.0.0.1:8000/app1/datasubmit/')
        return render(request, 'list1.html', {'data':a, 'all': obj1})
    return redirect('LOGIN')

def list2(request):
    if 'email' in request.session:
        if request.POST:
            Category_Name = request.POST['category']
            owner_Name = request.POST['owner']
            description_Of_Category = request.POST['description']
            price_Of_Product = request.POST['price']
            registration_date = request.POST['registration']
            rating_ = request.POST['rating']
            pro = Product()
            pro.CategoryName = Category_Name
            pro.ownerName = owner_Name
            pro.descriptionOfCategory = description_Of_Category
            pro.priceOfProduct = price_Of_Product
            pro.registration_date = registration_date
            pro.rating = rating_
            pro.save()
        return render(request, 'list2.html')
    return redirect('LOGIN')