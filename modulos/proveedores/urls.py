from django.urls import path
from .views import *

urlpatterns = {
    # PROVEEDORES
    path('list/<usuario>/', proveedores, name='proveedores'),
    path('detalle_proveedor/<usuario>/<proveedor>/', detalle_proveedor, name='detalle_proveedor'),
    path('editar_proveedor_vista/<usuario>/<proveedor>/', editar_proveedor_vista, name='editar_proveedor'),
    path('crear_proveedor_vista/<usuario>', crear_proveedor_vista, name='crear_proveedor_vista'),
    
    path('crear_proveedor/', crear_proveedor, name='crear_proveedor'),
    path('consultar_proveedores/', consultar_proveedores, name='consultar_proveedores'),
    path('consultar_proveedor_editar/', consultar_proveedor_editar, name='consultar_proveedor_editar'),
    path('actualizar_proveedor/', editar_proveedor, name='editar_proveedor'),
    
}