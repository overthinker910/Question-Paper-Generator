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
    path('preloader.html', views.preloader, name="preloader"),
    path('', include('gashfa.urls')),
    path('admin/', admin.site.urls),
]
