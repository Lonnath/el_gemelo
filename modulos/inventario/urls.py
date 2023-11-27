from django.urls import path
from .views import *

urlpatterns = {
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('consultar_productos/', consultar_productos, name='consultar_producto'),
    path('consultar_producto_editar/', consultar_producto_editar, name='consultar_producto_editar'),
    path('editar_producto/', editar_producto, name='editar_producto'),
}