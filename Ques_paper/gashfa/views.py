from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'main.html')
    #return HttpResponse('Its working')

def whereToGo(request):
    return render(request, 'where.html')

def aoa(request):
    return render(request, 'aoa.html')

def cPlusPlus(request):
    return render(request, 'c++.html')

def dataStruc(request):
    return render(request, 'data_str.html')

def dsm(request):
    return render(request, 'dsm.html')

def oop(request):
    return render(request, 'oop.html')

def pyth(request):
    return render(request, 'python.html')