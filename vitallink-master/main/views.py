from django.shortcuts import render
from django.http import HttpResponse
from .models import one
# Create your views here.

def index(response):
    return render(response,"main/index.html", {})

def choose(request):
    return render(request,'main/choose-login/block.html', {})

def login(request):
    return render(request,'main/login/login.html', {})

def signup(request):
    return render(request,'main/login/signup.html', {})