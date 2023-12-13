from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from modulos.proveedores.models import Proveedor
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoConsultaSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=255, required=True)
    activo = serializers.BooleanField(required=False)
    descripcion = serializers.CharField(max_length=255, required=False)
    precio = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    cantidad_disponible = serializers.IntegerField(required=False)
    proveedor = serializers.IntegerField(required=False)
   
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoConsultaEditarSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    id = serializers.IntegerField(required=True)
    nombre = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    activo = serializers.BooleanField(required=False)
    descripcion = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    precio = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    cantidad_disponible = serializers.IntegerField(required=False, allow_null=True)
    proveedor = serializers.IntegerField(required=False, allow_null=True)
   
    class Meta:
        model = Producto
        fields = '__all__'