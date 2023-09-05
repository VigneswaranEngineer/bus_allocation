from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request,'login.html',)

def registration(request):
    return render(request,'Registration.html')

def userpage(request):
    return render(request,'User Page.html')