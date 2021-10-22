from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, "input.html")

# def addition(request):
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     if num1.isdigit() and num2.isdigit():
#         a = int(num1)
#         b = int(num2)
#         res = a + b
#         return render(request, "result.html", {"result" : res})
#     else:
#         res = "Only digits are allowed for Addition operation"
#     return render(request, "input.html", {"result" : res})

# def subtraction(request):
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     if  num1.isdigit() and num2.isdigit():
#         a = int(num1)
#         b = int(num2)
#         res = a - b
#         return render(request, "result.html", {"result" : res})
#     else:
#         res = "Only digits are allowed for Subtraction operation"
#     return render(request, "input.html", {"result" : res})


# def multiplication(request):
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     if num1.isdigit() and num2.isdigit():
#         a = int(num1)
#         b = int(num2)
#         res = a * b
#         return render(request, "input.html", {"result" : res})
#     else:
#         res = "Only digits are allowed for Multiplication operation"
#     return render(request, "input.html", {"result" : res})


# def division(request):
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     if num1.isdigit() and num2.isdigit():
#         a = int(num1)
#         b = int(num2)
#         if b == 0:
#             res = "Zero division error"
#             return render(request, "input.html", {"result" : res})
#         else:
#             res = a / b
#             return render(request, "input.html", {"result" : res})
#     else:
#         res = "Only digits are allowed for Division operation"
#     return render(request, "input.html", {"result" : res})

def common(request):
    if request.POST:
        n1 = request.POST['num1']
        n2 = request.POST['num2']
        
        print(n1,n2)

        if 'add' in request.POST:
            ans = int(n1)+int(n2)
            print(ans)

        elif 'sub' in request.POST:
            ans = int(n1)-int(n2)
            print(ans)
        
        elif 'mul' in request.POST:
            ans = int(n1)*int(n2)
            print(ans)
        
        else:
            ans = int(n1)/int(n2)
            print(ans)

        return render(request,"input.html",{'ans':ans})
    return render(request,"input.html")


def faltu(request):
    if request.GET:
        a = float(request.GET["num1"])
        print(f"Value 1 is {a}")

        b = float(request.GET["num2"])
        print(f"Value 2 is {b}")

        if '+' == request.POST.get('operation'):
            try:
                ans1 = a + b
                ans = f"{a} + {b} = {ans1}"
                print(f"Addition is {ans}")
            except(ValueError):
                ans = "Only digits are allowed for Addition operation"
            return render(request, "input.html", {"ans":ans})

        elif '-' == request.POST.get('operation'):
            try:
                ans1 = a - b
                ans = f"{a} - {b} = {ans1}"
                print(f"Subtraction is {ans}")
            except (ValueError):
                ans = "Only digits are allowed for Subtraction operation"
            return render(request, "input.html", {"ans":ans})

        elif '*' == request.POST.get('operation'):
            try:
                ans1 = a * b
                ans = f"{a} x {b} = {ans1}"
                print(f"Multiplication is {ans}")
            except (ValueError):
                ans = "Only digits are allowed for Multiplication operation"
            return render(request, "input.html", {"ans":ans})
    
        elif '/' == request.POST.get('operation'):
            try:
                ans1 = a / b
                ans = f"{a} / {b} = {ans1}"
                print(f"Division is {ans}")
            except (ValueError):
                ans = "Only digits are allowed for Division operation"
            except (ZeroDivisionError):
                ans = "Denominator should not be 0"
            return render(request, "input.html", {"ans":ans})
    return render(request, "input.html")


