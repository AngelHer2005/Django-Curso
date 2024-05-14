from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
import random
import datetime

# VISTAS BASADAS EN CLASES, EN FUNCIONES Y CONFIGURACIÓN DE URLS:
# Funciones:
def holamundo(request):
    return HttpResponse("Hola Mundo")
# Clases:
class hola_mundo(View):
    def get(self, request):
        return HttpResponse("Hola Mundo")

# USO DE PLANTILLAS:
# Funciones:
def holamundoP(request):
    return render(request, "GESTION_URLS/plantilla.html")

# Clases:
class hola_mundoP(View):
    def get(self, request):
        return render(request, "GESTION_URLS/plantilla.html")

# PLANTILLAS, BLOQUES, HERENCIA, ETIQUETAS Y FILTROS:
#Bloques:
def bloque1(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/bloques/bloques1.html")

def bloque2(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/bloques/bloques2.html")

def bloque3(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/bloques/bloques3.html")

def bloque4(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/bloques/bloques4.html")


# Herencia:
def padre1(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia1/padre1.html")

def hija1(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia1/hija1.html")

def padre2(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia2/padre2.html")

def hija2(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia2/hija2.html")

def padre3(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia3/padre3.html")

def hija3(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia3/hija3.html")

def padre4(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia4/padre4.html")

def hija4(request):
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/herencia/herencia4/hija4.html")

# Etiquetas: 
def etiqueta1(request):
    probabilidad = random.choices([1,2], [0.4,0.6])[0]
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/etiquetas/etiquetas1.html", {"probabilidad":probabilidad})

def etiqueta2(request):
    lista = ["agua", "ropa", "juguega"]
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/etiquetas/etiquetas2.html", {"items":lista})

def etiqueta3(request):
    dic = {1:"a", 2:"b", 3:"c"}
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/etiquetas/etiquetas3.html", {"diccionario":dic})

def etiqueta4(request):
    personas = {"Juan": 25, "María": 17, "Pedro": 30, "Ana": 16}
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/etiquetas/etiquetas4.html", {"personas":personas})

# FIltros:
def filtro1(request):
    variable = "hola mundo"
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/filtros/filtro1.html", {"variable":variable})

def filtro2(request):
    lista = {1,2,3,4,5}
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/filtros/filtro2.html", {"lista":lista})

def filtro3(request):
    lorem_ipsum="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Necessitatibus libero, omnis assumenda quos magnam, at deleniti eveniet maiores quas a est pariatur dolorem velit tempore, enim esse eius consectetur fuga?"
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/filtros/filtro3.html", {"lorem_ipsum":lorem_ipsum})

def filtro4(request):
    dame_dia = datetime.datetime.now()
    return render(request, "BLOQUES, HERENCIA, ETIQUETAS Y FILTROS/filtros/filtro4.html", {"dia":dame_dia})