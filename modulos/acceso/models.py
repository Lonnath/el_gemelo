from django.db import models
from django.contrib.auth.models import User
class Bloqueos (models.Model):
    intentos = models.IntegerField(blank=False, null=False, default=0)
    bloqueo = models.BooleanField(blank=False, null=False, default=False)
    credenciales = models.ForeignKey(User, default=None,on_delete=models.DO_NOTHING)
    fecha_edicion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'bloqueos'

class Empleado(models.Model):
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
    usuario = models.ForeignKey(User, default=None,on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'empleados'