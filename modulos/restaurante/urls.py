from django.urls import path
from .views import *

urlpatterns = {
    # COMPRAS
    path('compras/<usuario>/', compras, name='compras'),
    path('realizar_compras/<usuario>/', realizar_compras, name='realizar_compras'),
    path('crear_compra/', crear_compra, name='crear_compra'),
    # VENTAS
    path('ventas/<usuario>/', ventas, name='ventas'),
    path('crear_venta/', crear_venta, name='crear_venta'),
    path('ver_detalle/<usuario>/<venta>/', ver_detalle_compra, name='ver_detalle'),
    # ANALISIS
    path('analisis/<usuario>/', analisis, name='analisis'),
    
}