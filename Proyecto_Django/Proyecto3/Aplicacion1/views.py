from django.shortcuts import render, redirect
from django.http import HttpResponse
from Aplicacion1.forms import *

# Ejemplo 1:
def success(request):
    return HttpResponse('Datos guardados correctamente!')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = ClienteForm1()
    return render(request, 'DJANGO ADMIN/plantilla.html', {'form': form})


# Ejemplo 2:

def crear_cliente2(request):
    if request.method == 'POST':
        form = ClienteForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = ClienteForm2()
    return render(request, 'DJANGO ADMIN/plantilla.html', {'form': form})

# Ejemplo 3:
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = ArticuloForm1()
    return render(request, 'DJANGO ADMIN/plantilla.html', {'form': form})

# Ejemplo 4:
def buscar_articulo(request):
    if request.method == 'POST':
        form = BuscarArticuloForm(request.POST)
        if form.is_valid():
            nombre_articulo = form.cleaned_data['nombre']
            articulos = Articulo.objects.filter(nombre__icontains=nombre_articulo)
            return render(request, 'DJANGO ADMIN/resultados_busqueda.html', {'articulos': articulos, 'query': nombre_articulo})
    else:
        form = BuscarArticuloForm()
    return render(request, 'DJANGO ADMIN/buscar_articulo.html', {'form': form})

# MANEJOS DE SESIONES
# EJEMPLO 1:
def crear_sesion(request):
    request.session["usuario"] = "Juan"
    nombre = request.session.get("usuario")
    return HttpResponse(f"Sesión creada<br>Bienvenido {nombre}")

# EJEMPLO 2:
def eliminar_ult_sesion(request):
    del request.session["usuario"]
    return HttpResponse("Sesión eliminada")

# EJEMPLO 3:
def limpiar_sesion(request):
    request.session.clear()
    return HttpResponse("Sesión limpia")

# EJEMPLO 4:
def ver_sesiones(request):
    mensaje=""
    for User, Idioma in request.session.items():
        mensaje+=f"{User=} - {Idioma=}<br>"
    return HttpResponse(mensaje)

# AUTENTICACIÓN Y AUTORIZACIÓN
# AUTENTICACIÓN
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            return redirect('logout')
        elif 'ver_cliente' in request.POST:
            return redirect('ver_modeloC')
    return render(request, 'index.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# AUTORIZACIÓN
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from Aplicacion1.models import Cliente

@login_required
@permission_required("Aplicacion1.view_cliente")
def ver_modeloC(request):
    datos = Cliente.objects.all()
    return render(request, 'AUTORIZACIÓN/vista_cliente.html', {"datos": datos})


