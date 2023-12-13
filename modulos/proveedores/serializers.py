from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from .models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorConsultaSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    activo = serializers.BooleanField(required=False, allow_null=True)
    numero_telefono = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    correo = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
    pais = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    codigo_postal = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    ciudad = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    direccion = serializers.CharField(required=False, allow_null=True, allow_blank=True)
   
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorConsultaEditarSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    id = serializers.IntegerField(required=True)
    nombre = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    activo = serializers.BooleanField(required=False)
    numero_telefono = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    correo = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
    pais = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    codigo_postal = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    ciudad = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    direccion = serializers.CharField(required=False, allow_null=True, allow_blank=True)
   
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorProductoConsultaSerializer(serializers.ModelSerializer):
    fecha_creacion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    fecha_edicion = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    id = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=255, required=False)
    activo = serializers.BooleanField(required=False)
    numero_telefono = serializers.CharField(required=False)
    correo = serializers.EmailField(required=False)
    pais = serializers.CharField(required=False)
    codigo_postal = serializers.CharField(required=False)
    ciudad = serializers.CharField(required=False)
    direccion = serializers.CharField(required=False)

    class Meta:
        model = Proveedor
        fields = '__all__'

