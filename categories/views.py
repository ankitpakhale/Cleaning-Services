from django.http import HttpResponse
from .models import *
from .forms import ProForm1
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
import razorpay
import datetime
import random

import smtplib
from email.message import EmailMessage

# Html To Pdf -------------------

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.http import HttpResponse
from django.views.generic import View

import pdfkit

# Html To Pdf -------------------

# Create your views here.

def main(request):
    return HttpResponse("This is a Main Page")

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
    if 'email' in request.session:
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
    return redirect('LOGIN')

def productUpdate(request, pk):
    if 'email' in request.session:
        prod= get_object_or_404(item, pk=pk)
        form = ProForm1(request.POST or None, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('PRODUCT')
        return render(request, 'editProduct1.html', {'form':form})
    return redirect('LOGIN')

def productDelete(request, pk):
    if 'email' in request.session:
        prod= get_object_or_404(item, pk=pk)   
        prod.delete() 
        return redirect('PRODUCT')
    return redirect('LOGIN')

def add_to_cart(request, d, s1):
    if 'email' in request.session:
        per=signUp.objects.get(email=request.session['email'])
        i=item.objects.get(id=d)
        if MyCart.objects.filter(person_id=per.pk, book_id=i.id, status=False).exists():
            
            # value = 'This Product is already in your CART, please choose another '
            # return(redirect('PRODUCTVIEW', d, {'value' : value}))
            
            # return render(request, 'showProduct1.html', {'value' : value})
    
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
    return redirect('LOGIN')

def removecart(request,d):
    if 'email' in request.session:
        o=signUp.objects.get(email=request.session['email'])
        y=get_object_or_404(MyCart,book=d,person=o.pk)
        y.delete()
        return(redirect('MYCART'))
    return redirect('LOGIN')

def cartorder(request):
    if 'email' in request.session:
        
        o_id = ''
        # r2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # r3 = random.choice('abcdefghijklmnopqrstuvwxyz')
        r2 = random.choice('1234567890')
        r3 = random.choice('1234567890')
        r4 = random.choice('1234567890')
        r6 = random.choice('1234567890')
        r7 = random.choice('1234567890')
        r8 = random.choice('1234567890')
        o_id = r2+r3+r4+r6+r7+r8
        print(f"Your Order ID is {o_id}")
        
        o=signUp.objects.get(email=request.session['email'])
        obj=MyCart.objects.filter(person=o.pk)
        l=[]
        q=[]
        p=0
        s=''
        for i in obj:
            l.append(i.book)
            q.append(i)
            s+=i.book.title+" Id="+str(i.book.id)+" Quantity ="+str(i.quantity)+','
            p=p+i.book.price*i.quantity
        
        print(l," ",q," ",p," ",s)

        if request.POST:
            n=request.POST['name']
            st=request.POST['state']
            ct=request.POST['city']
            ad=request.POST['address']
            pin=request.POST['pincode']
            ph=request.POST['phone']
            dat=request.POST['date']

            odr=Order()
            odr.oemail=request.session['email']
            odr.order_id= o_id
            odr.services=s
            odr.name=n
            odr.service_date=dat
            odr.contact=ph
            odr.amount=p
            odr.adddress=str(ad)+str(ct)+str(st)+'\n'+str(pin)
            
            odr.save()   

            amount= p
            print("Amount is ", amount)
            print(type(amount),type(p))

            client = razorpay.Client(auth=(
                "rzp_test_ov7fBmU4EJwsAn", 
                "AvmwLmd018H6gOgQrdeJPntX"
            ))

            payment = client.order.create({
                'amount': amount*100,
                'currency': 'INR',
                'payment_capture': '1'
            })         
            
            # ------------Bill Email Start----------------------
            sender_email = 'akp3067@gmail.com'
            reciv_email = o
            print(f"Customer's email address is {reciv_email}")
            
            msg = EmailMessage()
            msg.set_content(f'''     
            Thank you for taking our services.
            
            
            Your Order Details are:   

            Full Name       :  {n}  
            Order-Id        :  {o_id} 
            Amount          :  ₹{amount}/-
            Total Services  :  {s}  
            
            
            Thanks and Regards 
            Ankit Pakhale
            Chairman, MD and CEO of Washla Cleaning Services            
            ''')

            msg['Subject'] = 'Washla Cleaning Services'
            msg['From'] = sender_email
            # msg['To'] = reciv_email
            msg['To'] = 'ankitpakhale786@gmail.com'
            
            # Send the message via our own SMTP server.
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(
                "akp3067@gmail.com", 
                "Nailson1@0745"
            )

            server.send_message(msg)
            server.quit()
            messages.info(request, 'Message had been sent. Thank you for your notes')
            # ------------Bill Email End----------------------

            return(redirect('PAYMENT'))
            
        k=dict(zip(l,q))
        return(render(request,'orderpage.html',{'k':k,'p':p}))
    return redirect('LOGIN')

def payment(request):
    if 'email' in request.session:
        mainMsg = "Thanks for choosing our services"
        msg1 = "Payment"
        msg2 = "Successfully"
        msg3 = "Done"
        odrMsg = "My Order"
        return(render(request,'paymentSuccessPage.html',{'mainHeading':mainMsg,'paymentKey1':msg1, 'paymentKey2':msg2, 'paymentKey3':msg3, 'odrMsg':odrMsg}))
        # return(HttpResponse('Payment Successfully Done'))
    return redirect('LOGIN')

def customerOrder(request):
    if 'email' in request.session:
        Users = signUp.objects.get(email=request.session['email'])
        otdata = Order.objects.filter(name=Users)
        rec = set()
        for i in otdata:
            rec.add(i.order_id)
        rec = list(rec)
        rec.sort()
        return render(request,'custOrder.html',{'oids':rec})
    
        # return render(request,'custOrder.html')
    return redirect('LOGIN')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def viewSpecific(request,Orids):
    if 'email' in request.session:
        Users = signUp.objects.get(email=request.session['email'])
        otdata = Order.objects.filter(name=Users,order_id=Orids)
        tots = 0
        for i in otdata:
            tots += float(i.total)
        data = {'bilam':tots,'orders':otdata,'oids':Orids,'users':Users}
        pdf = render_to_pdf('GeneratePdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return redirect('login')


# def customerOrder0(request):
#     if 'email' in request.session:
        
#         o_id = ''
#         r2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#         r3 = random.choice('abcdefghijklmnopqrstuvwxyz')
#         r4 = random.choice('1234567890')
#         r6 = random.choice('1234567890')
#         r7 = random.choice('1234567890')
#         r8 = random.choice('1234567890')
#         o_id = r2+r3+r4+r6+r7+r8
#         print(o_id)
        
#         odr = Order()
#         odr.order_id = o_id

#         return render(request,'custAllOrders.html',{'allOrder':odr})
#     return redirect('LOGIN')


# def customerOrder1(request):
#     if 'email' in request.session:
#         Users = signUp.objects.get(email=request.session['email'])
#         otdata = MyCart.objects.filter(person=Users)
#         rec = set()
#         for i in otdata:
#             rec.add(i.order_id)
#         rec = list(rec)
#         rec.sort()
#         return render(request,'custAllOrders1.html',{'oids':rec})
#     return redirect('LOGIN') 


def donateMoney(request):
    if 'email' in request.session:
        user=signUp.objects.get(email=request.session['email'])
        model=DonateMoney.objects.create(
            person=user,
        )
        model.amount = request.POST.get('amount', 0)
        
        # amount= request.POST['amount']
        # print("Amount is ", amount)
        # client = razorpay.Client(auth=(
        #         "rzp_test_ov7fBmU4EJwsAn", 
        #         "AvmwLmd018H6gOgQrdeJPntX"
        # ))

        # payment = client.order.create({
        #     'amount': amount*100,
        #     'currency': 'INR',
        #     'payment_capture': '1'
        # })
        
        model.save() 
        return render(request,'donateMoney.html',{'model':model})        
    return redirect('LOGIN')
