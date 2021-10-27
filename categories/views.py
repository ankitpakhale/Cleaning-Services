from django.http import HttpResponse
from .models import *
from .forms import ProForm1
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages


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


def add_to_cart(request):
    if request.session.has_key('email'):
        per = signUp.objects.get(email=request.session['email'])
        item1 = MyCart.objects.filter(person__id=per.id, status=False)
        num = MyCart.objects.filter(person__id=per.id, status=False).count()
        total = 0
        for q in item1:
            total += q.book.price
        print(total)
        if request.method == 'POST':
            bid = request.POST['bid']
            print(bid)
            p = item.objects.get(id=bid)
            if MyCart.objects.filter(book__id=bid, person__id=per.id, status=False).exists():
                messages.warning(request, 'Item already in the cart')
                return render(request, 'single_product1.html', {'p': p, 'per': per})
            else:
                bk = get_object_or_404(item, id=bid)
                c = MyCart.objects.create(person=per, book=bk)
                c.save()
                messages.warning(request, 'Item has been added to cart')
                return render(request, 'single_product1.html', {'p': p, 'per': per})
        else:
            return render(request, 'checkout1.html', {'item': item1, 'num': num, 'per': per, 'total': total})
    else:
        messages.info(request, 'please login first to access the cart ')
        return redirect('LOGIN')

def remove_cart(request, id):
    if request.session.has_key('email'):
        y = get_object_or_404(MyCart, id=id)
        y.delete()
        return redirect('CART')
