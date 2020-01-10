from django.shortcuts import render
from django.http import HttpResponce

# Create your views here.
def home(request):
    return HttpResponce("Hello world")
    
