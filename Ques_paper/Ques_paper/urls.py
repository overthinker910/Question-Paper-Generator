"""Ques_paper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from gashfa import views
from django.contrib import admin
from django.urls import path, include
from gashfa.views import *

#we need to specify paths here when we want to link urls 
urlpatterns = [
    path('main.html',views.home ,name="home"),
    path('where.html',views.whereToGo ,name="whereToGo"),
    path('c++.html',views.cpp ,name="cpp"),
    path('oop.html',views.oop ,name="oop"),
    path('python.html',views.pyth ,name="pyth"),
    path('aoa.html',views.aoa ,name="aoa"),
    path('data_str.html',views.dataStruc ,name="datastr"),
    path('dsm.html',views.math ,name="dsm"),
    path('contact_us.html',views.contact ,name="contact_us"),
    path('advantages.html', views.advantages, name="advantages"), 
    path('location.html', views.locations_qp, name="location"), 
    path('preloader.html', views.preloader_python, name="preloader_python"),
    path('preloader.html', views.preloader_aoa, name="preloader_aoa"),
    path('priv.html', views.priv_pol, name="privacy_policy"),
<<<<<<< HEAD
    path('ques_pdf', views.ques_pdf, name="ques_pdf"),
=======
    path("ques_pdf", views.ques_pdf, name="ques_pdf"),  
>>>>>>> 4b9c9e4672dde3343e379e0947b73294e792ca69
    path('', include('gashfa.urls')),
    path('admin/', admin.site.urls),
]
