from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    edad = models.IntegerField()
    soltero = models.BooleanField()
    descripcion = models.TextField()
    cumpleaños = models.DateField()
    
    def __str__(self):
        return "El cliente %s tiene una edad de %s años y, por ende, es mayor de edad" % (self.nombre, self.edad)

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    seccion = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return "El artículo %s se encuentra en la sección %s" % (self.nombre, self.seccion)

""" En caso se necesiten los datos.
articulos = [
    Articulo(nombre='Leche', marca='Gloria', seccion='Lácteos', precio=3.50),
    Articulo(nombre='Arroz', marca='Costeño', seccion='Abarrotes', precio=2.50),
    Articulo(nombre='Azúcar', marca='Incaucho', seccion='Abarrotes', precio=2.00),
    Articulo(nombre='Pan', marca='Bimbo', seccion='Panadería', precio=1.50),
    Articulo(nombre='Aceite', marca='Primor', seccion='Abarrotes', precio=5.50),
    Articulo(nombre='Jabón', marca='Lavín', seccion='Limpieza', precio=1.20),
    Articulo(nombre='Papel Higiénico', marca='Elite', seccion='Limpieza', precio=2.80),
    Articulo(nombre='Cepillo de Dientes', marca='Colgate', seccion='Higiene', precio=3.00),
    Articulo(nombre='Shampoo', marca='Sedal', seccion='Higiene', precio=4.50),
    Articulo(nombre='Detergente', marca='Ace', seccion='Limpieza', precio=6.00),
]
"""