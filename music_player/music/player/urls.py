from django.contrib import admin
from django.urls import path, include
from .import views 
from .views import search

urlpatterns = [
    path('', views.search, name='search'),
]
