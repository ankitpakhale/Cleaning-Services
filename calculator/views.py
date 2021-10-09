from re import A
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
    a = float(request.POST['num1'])
    print(f"Value 1 is {a}")
    b = float(request.POST['num2'])
    print(f"Value 2 is {b}")

    if '+' == request.POST.get('operation'):
        try:
            ans = a + b
            print(f"Addition is {ans}")
        except (ValueError):
            ans = "Only digits are allowed for Addition operation"
        return render(request, "input.html", {"ans":ans})
    return render(request, "input.html")

    # elif '-' == request.POST.get('operation'):
    #     try:
    #         ans = a + b
    #         print(f"Addition is {ans}")
    #     except (ValueError):
    #         ans = "Only digits are allowed for Addition operation"
    #     return render(request, "input.html", {"ans":ans})
    # return render(request, "input.html")

    # elif '*' == request.POST.get('operation'):
    #     try:
    #         ans = a + b
    #         print(f"Addition is {ans}")
    #     except (ValueError):
    #         ans = "Only digits are allowed for Addition operation"
    #     return render(request, "input.html", {"ans":ans})
    # return render(request, "input.html")

    # elif '/' == request.POST.get('operation'):
    #     try:
    #         ans = a + b
    #         print(f"Addition is {ans}")
    #     except (ValueError):
    #         ans = "Only digits are allowed for Addition operation"
    #     return render(request, "input.html", {"ans":ans})
    # return render(request, "input.html")