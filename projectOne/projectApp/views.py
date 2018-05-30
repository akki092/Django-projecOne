from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>he is my friend!!!</em>')

def extension(request):
    kilo={'kg':'broken'}
    return render(request,'projectapp/index.html',context=kilo)