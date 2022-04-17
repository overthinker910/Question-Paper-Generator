from django.shortcuts import render
from django.http import HttpResponse
from ques_code import questions

# Create your views here.

def home(request):
    return render(request, 'main.html')
    #return HttpResponse('Its working')

def whereToGo(request):
    #return HttpResponse('Its working')
    return render(request, 'where.html')

def aoa(request):
    return render(request, 'aoa.html')

def cpp(request):
    return render(request, 'c++.html')

def dataStruc(request):
    return render(request, 'data_str.html')

def math(request):
    return render(request, 'dsm.html')

def oop(request):
    return render(request, 'oop.html')

def pyth(request):
    if request.method=="POST":
        questions.generate_ques()
    return render(request, 'python.html')