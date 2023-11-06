from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "myapp/index.html")

def image(request):
    return render(request, "myapp/image.html")

def advanced(request):
    return render(request,"myapp/advanced.html")