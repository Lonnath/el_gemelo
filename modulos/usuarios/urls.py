from django.urls import path
from .views import *

urlpatterns = {
    # USUARIOS
    path('list/<usuario>/', usuarios, name='usuarios'),
    path('detalle_usuario/<usuario>/<empleado>/', detalle_usuario, name='detalle_usuario'),
    path('editar_usuario/<usuario>/<empleado>/', editar_usuario, name='editar_usuario'),    
    path('crear_usuario/<usuario>/', crear_usuario, name='crear_usuario'), 
}