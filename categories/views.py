from django.http import HttpResponse
from .models import *
from .forms import ProForm1
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
import razorpay
import datetime


# Create your views here.

def main(request):
    return HttpResponse("This is a Home Page")

def product(request):
    if 'email' in request.session:
        obj1 = item.objects.all()
        a = ProForm1(request.POST)
        if a.is_valid():
            a.save()
            messages.success(request, 'Done')
        return render(request, 'product1.html', {'allProduct': obj1})
    return redirect('LOGIN')

def productView(request, pk):
    obj=item.objects.get(id=pk)
    qty=1
    if 'psub' in request.POST:
        if '+' in request.POST.get('psub'):
            qty=int(request.POST['qty'])+1
        else:
            qty=int(request.POST['qty'])
            if qty>1:
                qty=qty-1
    return(render(request,'showProduct1.html', {'object':obj,'qty':qty}))

def productUpdate(request, pk):
    prod= get_object_or_404(item, pk=pk)
    form = ProForm1(request.POST or None, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('PRODUCT')
    return render(request, 'editProduct1.html', {'form':form})

def productDelete(request, pk):
    prod= get_object_or_404(item, pk=pk)   
    prod.delete() 
    return redirect('PRODUCT')

def add_to_cart(request, d, s1):
    if 'email' in request.session:
        per=signUp.objects.get(email=request.session['email'])
        i=item.objects.get(id=d)
        if MyCart.objects.filter(person_id=per.pk, book_id=i.id, status=False).exists():
            return(HttpResponse('This Product is already in your CART, please choose another one'))
        else:
            cart=MyCart()
            cart.person=per
            cart.book=i
            cart.quantity=str(s1)
            cart.added_on=datetime.datetime.now()
            cart.save()
    return(redirect('PRODUCTVIEW',d))

def show_mycart(request):
    if 'email' in request.session:
        obj=signUp.objects.get(email=request.session['email'])
        all=MyCart.objects.filter(person=obj.pk)
        l=[]
        q=[]
        p=0
        for i in all:
            l.append(i.book)
            q.append(i)
            p=p+i.book.price*i.quantity
        k=dict(zip(l,q))   
        return(render(request,'mycartpage.html',{'k':k,'n':obj,'p':p}))

def removecart(request,d):
    if 'email' in request.session:
        o=signUp.objects.get(email=request.session['email'])
        y=get_object_or_404(MyCart,book=d,person=o.pk)
        y.delete()
        return(redirect('MYCART'))  

def cartorder(request):
    o=signUp.objects.get(email=request.session['email'])
    obj=MyCart.objects.filter(person=o.pk)
    l=[]
    q=[]
    p=0
    s=''
    for i in obj:
        print('1')
        l.append(i.book)
        q.append(i)
        s+=i.book.title+"  id="+str(i.book.id)+" Qunatity ="+str(i.quantity)+','
        p=p+i.book.price*i.quantity
    if request.POST:
        
        n=request.POST['name']
        st=request.POST['state']
        ct=request.POST['city']
        ad=request.POST['address']
        pin=request.POST['pincode']
        ph=request.POST['phone']
        dat=request.POST['date']
    
        iv=Order()
        iv.oemail=request.session['email']
        iv.services=s
        iv.name=n
        iv.service_date=dat
        iv.contact=ph
        iv.amount=p
        iv.adddress=str(ad)+str(ct)+str(st)+'\n'+str(pin)
        
        amount= p
        print("Amount is", amount)
        print(type(amount),type(p))
        # client = razorpay.Client(
        #     auth=("rzp_test_ov7fBmU4EJwsAn","AvmwLmd018H6gOgQrdeJPntX"))

        # payment = client.order.create({'amount':amount, 'currency': 'INR', 'payment_capture': '1'})
        
        client = razorpay.Client(auth=("rzp_test_ov7fBmU4EJwsAn", "AvmwLmd018H6gOgQrdeJPntX"))

        payment = client.order.create({
            'amount': amount*100,
            'currency': 'INR',
            'payment_capture': '1'
        })

        iv.save()
        return(redirect('PAYMENT'))
    
    k=dict(zip(l,q))
    return(render(request,'orderpage.html',{'k':k,'p':p}))

def payment(request):
    return(HttpResponse('success'))