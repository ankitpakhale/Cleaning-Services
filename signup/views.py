from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import signUp
from django.contrib import messages

# Create your views here.

def userSignUp1(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)
        Password = request.POST['password']
        print(Password)
        ConfirmPassword = request.POST['confirmPassword']
        print(ConfirmPassword)

        log = signUp()

        log.name = Name
        log.email = Email
        log.number = Number
        log.password = Password
        log.confirmPassword = ConfirmPassword
        log.save()
        
        if request.POST:
            pass1 = request.POST.get('password')
            pass2 = request.POST.get('confirmPassword')
            try:
                check = signUp.objects.get(password = pass1)
                if check.password == pass2:
                    return redirect('LOGIN')
                else:
                    msg = "Unmatched Password"
                return render(request, 'signup.html', {'msg' : msg})
            except:
                msg = "Matched Password"
                return render(request, 'login.html', {'msg' : msg})


        # return render(request, 'login.html')
        # messages.success(request, 'Done')
        # return HttpResponseRedirect('http://127.0.0.1:8000/signup/')
        return redirect('LOGIN')
        
    return render(request, 'signup.html')

def userSignUp(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)
        Password = request.POST['password']
        print(Password)
        ConfirmPassword = request.POST['confirmPassword']
        print(ConfirmPassword)

        try:
            if ConfirmPassword == Password:
                v = signUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.password = Password
                v.confirmPassword = ConfirmPassword
                v.save()
                return redirect('LOGIN')
            else:
                msg = 'Enter Same Password'
                return render(request , 'signup.html',{'msg':msg}) 

        except(NameError):
            return render(request, '404-error-page.html')
            
        except(TemplateDoesNotExist):
            return render(request, '404-error-page.html')
                
        finally:
            messages.success(request, 'Signup Successfully Done...')

    return render(request,'signup.html')

# def userLogin1(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            check = signUp.objects.get(email = em)
            if check.password == pass1:
                return redirect('HOME')
            else:
                msg = "Invalid Password"
            return render(request, 'login.html', {'msg' : msg})
            
        # except(NoReverseMatch):
            # return redirect('ERROR')
            # return redirect(request, 'WRONG', {'msg' : msg})

        except(NameError):
            return render(request, '404-error-page.html')
        except(TemplateDoesNotExist):
            return render(request, '404-error-page.html')
        
        except:
            msg = "Invalid Email ID"
            return render(request, 'login.html', {'msg' : msg})
    return render(request, 'login.html')

def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            check = signUp.objects.get(email=em)
            if check.password == pass1:
                
                nameMsg = signUp.objects.all()

                name = f"Welcome {nameMsg}"
                # return redirect('HOME')
                return render(request,'home.html', {'key':name})
            else:
                msg = 'Invalid Password'
                return render(request , 'wrongPassword.html',{'msg':msg}) 

        # except(NameError):
        #     return render(request, '404-error-page.html')
        # except(TemplateDoesNotExist):
        #     return render(request, '404-error-page.html')

        except:
            msg = 'Invalid Email ID'
            return render(request,'wrongPassword.html', {'msg':msg})

    return render(request,'login.html')

def confirm(request):
    if request.POST:
        data = request.POST['conf']
        try:
            valid = signUp.objects.get(email=data)
            if valid:
                request.session['email'] = valid.email
                return redirect('FORGOT')
            else:
                return HttpResponse('Wrong Answer')    
        except:
            return HttpResponse('Wrong Answer')
    return render(request,'confirm.html')

def forgot(request):
    if 'email' in request.session:
        if request.POST:
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            
            if pass1 == pass2:
                obj = signUp.objects.get(email=request.session['email'])
                obj.password = pass1
                obj.confirmPassword = pass2
                obj.save()
                del request.session['email']
                return redirect('LOGIN')
            else:
                messages.add_message(request, messages.ERROR, 'Enter Same Password')
            
        return render(request,'forgot.html')
    return redirect('LOGIN')