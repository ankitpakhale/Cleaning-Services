from django.http import HttpResponse
from .models import *
from .forms import ProForm1
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
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
    prod= get_object_or_404(item, pk=pk)
    return render(request, 'showProduct1.html', {'object':prod})

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

def add_to_cart(request, d):
    if 'email' in request.session:
        per=signUp.objects.get(email=request.session['email'])
        i=item.objects.get(id=d)
    
        if MyCart.objects.filter(person_id=per.pk, book_id=i.id, status=False).exists():
            return(HttpResponse('This Product is already in your CART, please choose another one'))
    
        else:
            cart=MyCart()
            cart.person=per
            cart.book=i
            cart.added_on=datetime.datetime.now()
            cart.save()
    return(redirect('PRODUCTVIEW',d))


def show_mycart(request):
    if 'email' in request.session:
        obj=signUp.objects.get(email=request.session['email'])
        all=MyCart.objects.filter(person=obj.pk)
        l=[]
        p=0
        for i in all:
            l.append(i.book)
            p=p+i.book.price
        return(render(request,'mycartpage.html',{'al':l,'n':obj,'p':p}))

def removecart(self,d):
    if 'email' in self.session:
        o=signUp.objects.get(email=self.session['email'])
        y=get_object_or_404(MyCart,book=d,person=o.pk)
        y.delete()
        return(redirect('MYCART'))  
