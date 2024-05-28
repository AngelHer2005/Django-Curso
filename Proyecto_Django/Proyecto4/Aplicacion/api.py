from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import ArticuloSerializer
from rest_framework import generics


class ArticuloAPIView(APIView):
    def get(self, request):
        art = Articulo.objects.all()
        serializer = ArticuloSerializer(art, many= True)
        return Response(serializer.data)

from django_ratelimit.decorators import ratelimit

class Filtrado(generics.ListAPIView):
    art = Articulo.objects.all()  
    serializer_class = ArticuloSerializer
    @ratelimit(key='ip', method=ratelimit.ALL, block=True)
    def get_queryset(self):
        art = self.art 
        seccion = self.request.query_params.get('seccion', None)
        if seccion:
            art = art.filter(seccion=seccion)
        return art
        
# ROUTERS:
from rest_framework import viewsets

class ArticuloViewSet(viewsets.ViewSet):
    @ratelimit(key='ip', rate='5/m', method=ratelimit.ALL, block=True)
    def list(self, request):
        queryset = Articulo.objects.all()
        seccion = request.query_params.get('seccion', None)
        if seccion:
            queryset = queryset.filter(seccion=seccion)
        serializer = ArticuloSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
# AJAX:
from rest_framework.response import Response
from rest_framework.views import APIView

class AJAXView(APIView):
    def get(self, request):
        data = {'mensage': 'Este es otro mensaje!'}
        return Response(data)