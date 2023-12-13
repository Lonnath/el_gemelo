from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True, blank=True, null=True)
    numero_telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(unique=False, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'proveedores'

    def update_proveedor (self, nombre=None, activo=None, numero_telefono=None, correo=None, pais=None, codigo_postal=None, ciudad=None, direccion=None):
        if nombre:
            self.nombre = nombre
        if activo:
            self.activo = activo
        if numero_telefono:
            self.numero_telefono = numero_telefono
        if correo:
            self.correo = correo
        if pais:
            self.pais = pais
        if codigo_postal:
            self.codigo_postal = codigo_postal
        if ciudad:
            self.ciudad = ciudad
        if direccion:
            self.direccion = direccion