from django.urls import path
from .views import *

urlpatterns = {
    path('', acceso, name='login'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('recovery_password/', recovery_password, name='recovery'),
    path('actualizar_usuario/', actualizar_usuario, name='actualizar_usuario')
}