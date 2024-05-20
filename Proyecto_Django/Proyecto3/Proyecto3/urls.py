"""
URL configuration for Proyecto3 project.

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
from django.contrib.auth.views import LoginView, LogoutView
from Aplicacion1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # AUTENTICACIÓN/LOGIN Y LOGOUT
    path('', home, name="home"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    # DJANGO ADMIN
    path("crear/", crear_cliente),
    path("success/", success),
    path("crear2/", crear_cliente2),
    path("crear3/", crear_articulo),
    path("buscar/", buscar_articulo),
    # MANEJOS DE SESIONES
    path("crearS/", crear_sesion),
    path("eliminarS/", eliminar_ult_sesion),
    path("limpiarS/", limpiar_sesion),
    path("verS/", ver_sesiones),
    # AUTENTICACIÓN Y AUTORIZACIÓN
    path("verS/", ver_sesiones),
    path("modeloCliente/", ver_modeloC, name="modeloC"),
]
