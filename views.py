from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hi, This is our First Django Website");
   return render(request, 'index.html')

def about(request):
    return HttpResponse("Hi, About Page");

def contact(request):
    return HttpResponse("Hi, Contact Page");