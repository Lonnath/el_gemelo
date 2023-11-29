from django.db import models

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