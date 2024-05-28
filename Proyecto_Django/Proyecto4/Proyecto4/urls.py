"""
URL configuration for Proyecto4 project.

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
from django.urls import path, include
from Aplicacion.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("articulo/", ArticuloAPIView.as_view(), name="Articulo_api"),
    path("Filtrado/", Filtrado.as_view(), name="Filtrado_api"),
    #ROUTERS
    path("ArticuloV/", include("Aplicacion.router")),
    # AJAX
    path("Ajax/", AJAXView.as_view(), name="AJAX")
]
