from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse("This is a Home Page")