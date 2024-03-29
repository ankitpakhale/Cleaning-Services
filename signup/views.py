from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import signUp
from django.contrib import messages
import random
import smtplib
from email.message import EmailMessage

# Create your views here.

def userSignUp(request):
    if request.POST:
        Name = request.POST['name']
        print(Name) 
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)
        print(len(Number))
        Password = request.POST['password']
        print(Password)
        ConfirmPassword = request.POST['confirmPassword']
        print(ConfirmPassword)
        try:
            if (len(Number) > 10) or (len(Number) < 10) :
                msg = "Phone number should be equal to 10 characters" 
                return render(request , 'signup.html',{'msg':msg}) 
            
            elif (len(Password) < 8):
                msg = "Password should be greater than 8 characters" 
                return render(request , 'signup.html',{'msg':msg}) 
            
            elif (ConfirmPassword == Password) & (Number == 10):
                v = signUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.confirmPassword = ConfirmPassword
                v.save()
                return redirect('LOGIN')
            else:
                msg = 'Please Enter Same Password'
                return render(request , 'signup.html',{'msg':msg}) 
        except(NameError):
            return render(request, '404-error-page.html')
        
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')
        
        finally:
            messages.success(request, 'Signup Successfully Done...')
    return render(request,'signup.html')

def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            check = signUp.objects.get(email = em)
            print("Email is ",em)

            if (em == "" or pass1 == ""):
                msg = "Please fill all the given fields" 
                return render(request , 'login.html',{'msg':msg}) 



            # nav bar HEADER NAME PENDING
            elif check.password == pass1:
                request.session['email'] = check.email
                nameMsg = signUp.objects.all()
                print('User logged in')
                # return redirect('HOME')
                return render(request,'home.html', {'key':nameMsg})    
            else:
                msg = 'Invalid Password'
                # return render(request , 'wrongPassword.html',{'msg':msg}) 
                return render(request , 'login.html',{'msg':msg}) 

        except(NameError):
            return render(request, '404-error-page.html')

        except Exception:
            msg = 'Invalid Email ID'
            # return render(request,'wrongPassword.html', {'msg':msg})
            return render(request,'login.html', {'msg':msg})

    return render(request,'login.html')

def forgot(request):
    if request.POST:
        data = request.POST['email']
        print(data)
        try:
            return sendMail(data, request)
        except Exception:
            return HttpResponse('<a href=""> You Have Entered Wrong Email Id... </a>')
    return render(request,'forgot.html')

def sendMail(data, request):
    valid = signUp.objects.get(email=data)
    print(valid)
    otp = ''
    rand = random.choice('0123456789')
    rand1 = random.choice('0123456789')
    rand2 = random.choice('0123456789')
    rand3 = random.choice('0123456789')
    otp = rand + rand1 + rand2 + rand3
    print(f"Your OTP is {otp}")
    msg = EmailMessage()
    msg.set_content(f'''     
            Thank you for contacting with us.
            Your OTP is {otp}
            ''')
    msg['Subject'] = 'Washla Cleaning Services'
    msg['From'] = 'manage.py.flush@gmail.com'
    msg['To'] = 'manage.py.flush@gmail.com'
    # msg['To'] = '{valid}'
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("manage.py.flush@gmail.com", "0")
    server.send_message(msg)
    server.quit()
    request.session['otp'] = otp
    return redirect('OTPCHECK')

def otpCheck(request):
    if 'otp' not in request.session.keys():
        return redirect('LOGIN')
    if request.POST:
        otp1 = request.POST['otpuser']
        print(f"OTP1 is {otp1}")
        otp = request.session['otp']
        print(f"OTP is {otp}")
        if otp1 == otp:
            # del request.session['otp']
            print("You Are Ready to Create New Password...")

            # user = signUp.objects.get(email = otp1)
            # request.session['email'] = user.email

            return redirect('NEWPASS')
        else:
            del request.session['otp']
            return redirect('FORGOT')
    return render(request,'otpCheck.html')

def newPassword(request):
    print("Inside New Pass FUNCTION")
    # if 'otp' in request.session.keys():
    if 'email' in request.session:
        print("Inside New Pass if CONDITION")
        if request.POST:
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            print(f"{pass1} : {pass2}")
            if pass1 == pass2:
                return createNewPassword(request, pass1, pass2)
            else:
                return HttpResponse("<h1>Password must be same</h1>")
        return render(request,'newPass.html')
    return redirect('LOGIN')


def createNewPassword(request, pass1, pass2):
    print("Both password is correct")
    # obj = signUp.objects.get(email =  request.POST.get('email'))
    obj = signUp.objects.get(email = request.session['email'])

    obj.password = pass1
    obj.confirmPassword = pass2
    obj.save()
    del request.session['otp']
    # return redirect('HOME')
    return redirect('LOGIN')

def userLogOut(request):
    if 'email' in request.session:
        del request.session['email']
        print('User logged out')
    else:
        print('session is not present')
    return redirect('LOGIN')
