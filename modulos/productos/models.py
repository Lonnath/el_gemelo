from django.db import models
from modulos.proveedores.models import Proveedor
from rest_framework.exceptions import ValidationError

class Producto (models.Model):
    nombre = models.TextField(blank=True, null = True)
    descripcion = models.TextField(blank=True, null = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null = True)
    cantidad_disponible = models.IntegerField(blank=True, null = True)
    proveedor = models.ForeignKey(Proveedor, related_name='proveedor', on_delete=models.CASCADE, null=True, blank=True)
    activo = models.BooleanField(default=True)
    tiempo_entrega_estimada = models.TextField(blank=True, null = True)
    class Meta:
        db_table = 'producto'

    def update_producto(self, nombre=None, descripcion=None, precio = None, cantidad_disponible = None, proveedor = None, activo = None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if precio:
            self.precio = precio
        if cantidad_disponible:
            self.cantidad_disponible = cantidad_disponible
        if proveedor:
            try:
                proveedor_actualizar = Proveedor.objects.get(id=proveedor)
            except Proveedor.DoesNotExist:
                raise ValidationError("Proveedor no encontrado, edite nuevamente el producto.")
            self.proveedor = proveedor_actualizar
        if activo:
            self.activo = activo
