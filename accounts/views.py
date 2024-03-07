from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('home')

def products(requet):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('Customer')