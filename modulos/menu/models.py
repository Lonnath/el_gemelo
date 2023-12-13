from django.db import models
from modulos.productos.models import Producto
from django.core.exceptions import ValidationError
from django.utils import timezone
from modulos.acceso.models import Empleado


class Item(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    def disponible(self):
        if not self.activo:
            return False
        for item_preparacion in self.preparacion.all():
            if item_preparacion.cantidad_requerida > item_preparacion.producto.cantidad_disponible:
                return False
        return True

    class Meta:
        db_table = 'item_menu'

class Menu(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=255)
    items_menu = models.ManyToManyField(Item)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'menu'

class Preparacion(models.Model):
    cantidad_requerida = models.IntegerField(blank=False, null=False, default=1)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='Necesidad')
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'preparacion_item_menu'

