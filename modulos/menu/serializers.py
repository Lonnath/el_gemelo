from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from modulos.productos.models import Producto
from .models import *

class ItemSerializer(serializers.Serializer):
    preparaciones = serializers.JSONField()
    nombre = serializers.CharField(required=True)
    descripcion = serializers.CharField(required=True)
    precio = serializers.DecimalField(max_digits=10, decimal_places=2)
    activo = serializers.BooleanField(required=True)
    categoria = serializers.CharField(required=True)
    
    def create(self, validated_data):
        item = Item(nombre=validated_data['nombre'], descripcion=validated_data['descripcion'], precio=validated_data['precio'], activo=validated_data['activo'], 
            categoria=validated_data['categoria'])
        item.save()
        for preparacion in validated_data['preparaciones']:
            producto_temporal = Producto.objects.get(id=preparacion['producto'])
            preparacion_crear = Preparacion(cantidad_requerida=preparacion['cantidad_requerida'], producto=producto_temporal, item=item)
            preparacion_crear.save()
        return item

class ItemsConsultaSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    nombre = serializers.CharField(required=False)
    descripcion = serializers.CharField(required=False)
    precio = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    activo = serializers.BooleanField(required=False)
    class Meta:
        model = Item
        fields = '__all__'
