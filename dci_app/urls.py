#Criando uma urls para meu app
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('search/', views.search_results, name="search_results"),
    path('error/', views.error, name="error"),
    path('formulario/', views.formulario, name="formulario")

]
