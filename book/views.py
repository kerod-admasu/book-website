# file: appName/views.py

from django.shortcuts import render, HttpResponse #import HttpResponse
from .models import*
# Create your views here.


def home(request):
  
   books = Product.objects.all()
   
   data ={
      
      'books':books,
   }
   
   return render(request, 'home.html',data)

def about(request):
   return render(request,'about.html')

def contact_us(request):
   return render(request,'contact.html')

def books(request):
   return render(request,'books.html')


