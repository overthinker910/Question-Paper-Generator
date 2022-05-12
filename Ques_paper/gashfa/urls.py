from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("whereToGo", views.whereToGo, name='whereToGo'),
    path("algorithm", views.aoa, name='algorithm'),
    path("python", views.pyth, name='python'),
    path("oop", views.oop, name='oop'),
    path("data_str", views.dataStruc, name='data_str'),
    path("math", views.math, name='math'),
    path("cpp", views.cpp, name='cpp'),
    path("locations_qp", views.locations_qp, name='locations_qp'),
    path("privacy_policy", views.priv_pol, name='priv_pol'),
    path("preloader_aoa", views.preloader_aoa, name='preloader_aoa'),
    path("preloader_python", views.preloader_python, name='preloader_python'),
    path("preloader_cpp", views.preloader_cpp, name='preloader_cpp'),
    path("preloader_datastr", views.preloader_datastr, name='preloader_datastr'),
    path("preloader_dsm", views.preloader_dsm, name='preloader_dsm'),
    path("preloader_oop", views.preloader_oop, name='preloader_oop'),   
    path("ques_pdf",views.ques_pdf,name="ques_pdf"),
]