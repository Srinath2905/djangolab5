from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


""" def index(request):
    return HttpResponse("Hello, world") """
from django.http import JsonResponse

def index(request):
    responseData = {
        "Message" : "Hello World!"
    }
    return JsonResponse(responseData)


def home(request):
    return render(request,'home.html')