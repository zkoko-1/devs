from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html',{})

def default_page(request):
    return HttpResponseRedirect('home/')

def base_page(request):
    return render(request,'base.html',{})