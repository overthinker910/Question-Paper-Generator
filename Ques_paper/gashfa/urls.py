from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/where', views.whereToGo, name='where'),
    path('/aoa', views.aoa, name='aoa'),
    path('/python', views.pyth, name='python'),
    path('/oop', views.oop, name='oop'),
    path('/data_str', views.dataStruc, name='data_str'),
]