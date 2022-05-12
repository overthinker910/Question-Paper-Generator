import webbrowser
from django.shortcuts import redirect, render
from django.http import HttpResponse
from urllib3 import HTTPResponse
from ques_code import questions
<<<<<<< HEAD
import webbrowser
=======
import os, subprocess
>>>>>>> 4b9c9e4672dde3343e379e0947b73294e792ca69

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

# def preloader(request):
#     return render(request, 'preloader.html')

def locations_qp(request):
    #return HttpResponse('Its working')
    return render(request, 'location.html')

def priv_pol(request):
    #return HttpResponse('Its working')
    return render(request, 'priv.html')

def preloader_aoa(request):
    if request.method=="POST":
        questions.generate_ques("aoa_excel")
    return render(request, 'preloader.html')

def preloader_python(request):
    if request.method=="POST":
        questions.generate_ques("python_excel")
    return redirect(request, 'preloader.html')

def preloader_cpp(request):
    if request.method=="POST":
        questions.generate_ques("cpp_excel")
    return render(request, 'preloader.html')

def preloader_datastr(request):
    if request.method=="POST":
        questions.generate_ques("data_struct_excel")
    return render(request, 'preloader.html')

def preloader_dsm(request):
    if request.method=="POST":
        questions.generate_ques("dsm_excel")
    return render(request, 'preloader.html')

def preloader_oop(request):
    if request.method=="POST":
        questions.generate_ques("oop_excel")
    return render(request, 'preloader.html')

def ques_pdf(request):
<<<<<<< HEAD
    def test():
        path="pdf_1.pdf"
        return webbrowser.open_new(path)
    test()
    return render(request, 'where.html')

=======
    path = "pdf_1.pdf"
    # os.system(path)
<<<<<<< HEAD
    webbrowser.open_new(path)
    return redirect('where.html')
=======
    return webbrowser.open_new(path)
    
>>>>>>> 4b9c9e4672dde3343e379e0947b73294e792ca69
>>>>>>> ec253fcbebe8ea19e274488887fd4dbb4d574758
