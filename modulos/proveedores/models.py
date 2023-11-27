from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    numero_telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=False)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()
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