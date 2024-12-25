from django.contrib import admin
from django.urls import path,include, re_path
from . import views

urlpatterns = [
    
    path('', views.searchResult, name='search_result'),
    path('create_result', views.createResult, name='create_result'),




]