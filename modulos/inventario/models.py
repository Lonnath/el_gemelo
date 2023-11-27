from django.db import models
from modulos.proveedores.models import Proveedor
from rest_framework.exceptions import ValidationError

class Producto (models.Model):
    nombre = models.TextField(blank=False, null = False)
    descripcion = models.TextField(blank=False, null = False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField(blank=False, null = False)
    proveedor = models.ForeignKey(Proveedor, related_name='proveedor', on_delete=models.CASCADE, null=True, blank=True)
    activo = models.BooleanField(default=True)
    
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

class CompraProductos(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField(blank=False, null=False, default=1)
    
    class Meta:
        db_table = 'compras_productos'