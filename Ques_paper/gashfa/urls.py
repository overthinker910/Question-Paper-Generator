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
<<<<<<< HEAD
=======
    path("privacy_policy", views.priv_pol, name='priv_pol'),
    path("preloader", views.preloader, name='preloader'),
    
>>>>>>> 085f0c2270d2f151a8f900e8f8bcf5ea4a7b464e
]