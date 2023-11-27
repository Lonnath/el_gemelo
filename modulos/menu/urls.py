from django.urls import path
from .views import *

urlpatterns = {
    path('crear_item/', crear_item, name='crear_item'),
    path('consultar_items/', consultar_items, name='consultar_item'),
    path('consultar_item_editar/', consultar_item_editar, name='consultar_item_editar'),
    path('editar_item/', editar_item, name='editar_item'),
}