from django.urls import path
from .views import *

urlpatterns = {
    path('crear_proveedor/', crear_proveedor, name='crear_proveedor'),
    path('consultar_proveedores/', consultar_proveedores, name='consultar_proveedores'),
    path('consultar_proveedor_editar/', consultar_proveedor_editar, name='consultar_proveedor_editar'),
    path('editar_proveedor/', editar_proveedor, name='editar_proveedor'),
    
}