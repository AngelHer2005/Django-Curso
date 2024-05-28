from rest_framework import serializers
from .models import *

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'