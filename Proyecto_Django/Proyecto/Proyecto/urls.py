"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Proyecto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # VISTAS BASADAS EN CLASES, EN FUNCIONES Y CONFIGURACIÓN DE URLS
    path('funciones/', holamundo),
    path('clases/', hola_mundo.as_view()),
    path('funcionesP/', holamundoP),
    path('clasesP/', hola_mundoP.as_view()),
    # BLOQUES, HERENCIA, ETIQUETAS Y FILTROS
    #Bloque:
    path('bloque1/', bloque1),
    path('bloque2/', bloque2),
    path('bloque3/', bloque3),
    path('bloque4/', bloque4),
    #Herencia:
    path('padre1/', padre1),
    path('hija1/', hija1),
    path('padre2/', padre2),
    path('hija2/', hija2),
    path('padre3/', padre3),
    path('hija3/', hija3),
    path('padre4/', padre4),
    path('hija4/', hija4),
    #Etiqueta
    path('etiqueta1/', etiqueta1),
    path('etiqueta2/', etiqueta2),
    path('etiqueta3/', etiqueta3),
    path('etiqueta4/', etiqueta4),
    #Filtro
    path('filtro1/', filtro1),
    path('filtro2/', filtro2),
    path('filtro3/', filtro3),
    path('filtro4/', filtro4)
]
