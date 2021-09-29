from django.shortcuts import render, redirect
from .models import signUp

# Create your views here.

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

        log = signUp()

        log.name = Name
        log.email = Email
        log.number = Number
        log.password = Password
        log.confirmPassword = ConfirmPassword
        log.save()

        # messages.success(request, 'Done')
        # return HttpResponseRedirect('http://127.0.0.1:8000/signup/')
        return redirect('HOME')
    return render(request, 'signup.html')

# def userLogin(request):
#     if request.POST:
#         Email = request.POST['email']
#         print(Email)
#         Password = request.POST['password']
#         print(Password)
#         log = signUp()
#         log.email = Email
#         log.password = Password
#         log.save()
#         # messages.success(request, 'Done')
#         # return HttpResponseRedirect('http://127.0.0.1:8000/signup/login/')
#         return redirect('HOME')
#     return render(request, 'login.html')

def userLogin(request):
    if request.POST:
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
        try:
            check = signUp.objects.get(email = em)
            if check.password == pass1:
                return redirect('HOME')
            else:
                msg = "Wrong Password"
            return render(request, 'login.html', {'msg' : msg})
        except:
            msg = "Wrong Email ID"
            return render(request, 'login.html', {'msg' : msg})
    return render(request, 'login.html')