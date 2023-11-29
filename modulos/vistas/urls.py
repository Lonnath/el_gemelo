from django.urls import path
from .views import *

urlpatterns = {
    path('', index, name='index'),
    # MENU
    path('menu/', menu, name='menu'),
    # PRODUCTOS
    path('productos/', productos, name='productos'),
    path('detalle_producto/', detalle_producto, name='detalle_producto'),
    # PROVEEDORES
    path('proveedores/', proveedores, name='proveedores'),
    path('detalle_proveedor/', detalle_proveedor, name='detalle_proveedor'),
    path('editar_proveedor/', editar_proveedor, name='editar_proveedor'),
    # USUARIOS
    path('usuarios/', usuarios, name='usuarios'),
    path('detalle_usuario/', detalle_usuario, name='detalle_usuario'),
    path('editar_usuario/', editar_usuario, name='editar_usuario'),
    # COMPRAS
    path('compras/', compras, name='compras'),
    # VENTAS
    path('ventas/', ventas, name='ventas'),
    # ANALISIS
    path('analisis/', analisis, name='analisis'),
    
}