from django.urls import path
from .views import *

urlpatterns = {
    
    # PRODUCTOS
    path('list/<usuario>/', productos, name='productos'),
    path('detalle_producto/<usuario>/<producto>/', detalle_producto, name='detalle_producto'),
    path('crear_producto_vista/<usuario>/', crear_producto_vista, name='crear_producto_vista'),
    path('editar_producto_vista/<usuario>/<producto>/', editar_producto_vista, name='editar_producto_vista'),
    
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('consultar_productos/', consultar_productos, name='consultar_producto'),
    path('consultar_producto_editar/', consultar_producto_editar, name='consultar_producto_editar'),
    path('editar_producto/', editar_producto, name='editar_producto'),
}