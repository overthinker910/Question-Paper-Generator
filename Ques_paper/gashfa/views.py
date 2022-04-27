from django.shortcuts import render
from django.http import HttpResponse
from ques_code import questions

# Create your views here.

def home(request):
    return render(request, 'main.html')
    #return HttpResponse('Its working')

def contact(request):
    return render(request, 'contact_us.html')
    #return HttpResponse('Its working')

def advantages(request):
    return render(request, 'advantages.html')

def whereToGo(request):
    #return HttpResponse('Its working')
    return render(request, 'where.html')

def aoa(request):
    if request.method=="POST":
        questions.generate_ques('aoa_excel')
    return render(request, 'aoa.html')

def cpp(request):
    if request.method=="POST":
        questions.generate_ques('cpp_excel')
    return render(request, 'c++.html')

def dataStruc(request):
    if request.method=="POST":
        questions.generate_ques('data_struct_excel')
    return render(request, 'data_str.html')

def math(request):
    if request.method=="POST":
        questions.generate_ques('dsm_excel')
    return render(request, 'dsm.html')

def oop(request):
    if request.method=="POST":
        questions.generate_ques('oop_excel')
    return render(request, 'oop.html')

def pyth(request):
    if request.method=="POST":
        questions.generate_ques('python_excel')
    return render(request, 'python.html')

def preloader(request):
    return render(request, 'preloader.html')

def locations_qp(request):
    #return HttpResponse('Its working')
    return render(request, 'location.html')

def priv_pol(request):
    #return HttpResponse('Its working')
    return render(request, 'priv.html')

def preloader2(request):
    if request.method=="POST":
        questions.generate_ques('dsm_excel')
    return render(request, 'dsm.html')