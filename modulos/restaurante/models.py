from django.db import models
from modulos.productos.models import Producto
class Restaurante(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    numero_telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    horario_atencion_inicio = models.TimeField()
    horario_atencion_cierre = models.TimeField()
    
    class Meta:
        db_table = 'restaurante'



class CompraProductos(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    referencia_compra = models.CharField(max_length=50, unique=True, default='CI-')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(default=0, blank=True, null=True)
    
    class Meta:
        db_table = 'compras_productos'



class VentaProducto(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    referencia_venta = models.CharField(max_length=50, unique=True, default='VP-')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    dinero_ingresado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        db_table = 'venta_productos'

class DetalleVentaProducto(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    venta_producto = models.ForeignKey(VentaProducto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table = 'detalle_venta_productos'
    