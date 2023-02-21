from django.contrib import admin
from django.urls import path, include
from data_uk import views

urlpatterns = [
    path('', views.getPrice, name="get_data"),
]
