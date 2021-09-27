from django.shortcuts import render, redirect
from .models import login

# Create your views here.

def userLogin1(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)

        log = login()
        log.name = Name
        log.email = Email
        log.number = Number
        log.save()
        # messages.success(request, 'Done')
        # return HttpResponseRedirect('http://127.0.0.1:8000/login/login1')
        return redirect('HOME')
    return render(request, 'login1.html')

def userLogin(request):
    if request.POST:
        Name = request.POST['name']
        print(Name)
        Email = request.POST['email']
        print(Email)
        Number = request.POST['number']
        print(Number)

        log = login()
        log.name = Name
        log.email = Email
        log.number = Number
        log.save()
        # messages.success(request, 'Done')
        # return HttpResponseRedirect('http://127.0.0.1:8000/login/login/')
        return redirect('HOME')
    return render(request, 'login.html')

