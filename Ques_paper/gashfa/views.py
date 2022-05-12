import webbrowser
from django.shortcuts import redirect, render
from django.http import HttpResponse
from urllib3 import HTTPResponse
from ques_code import questions
import webbrowser

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
        level = id
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
    return render(request, 'preloader.html')

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
    path = "pdf_1.pdf"
    path1 = "pdf_2.pdf"
    # os.system(path)
    webbrowser.open_new(path)
<<<<<<< HEAD
    webbrowser.open_new(path1)
    return redirect('where.html')
    
=======
    return redirect('where.html')
>>>>>>> f4f26d40b501988f905f16d4ac0e500dc4f20f50
