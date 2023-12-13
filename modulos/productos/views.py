from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.shortcuts import render
from .models import *
from modulos.proveedores.models import Proveedor
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import json
import copy
from django.contrib.auth.models import User
from modulos.productos.models import Producto
from modulos.productos.serializers import *
@csrf_exempt
def productos(request, usuario):
    banner_title = "Productos"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
    })
    productos = Producto.objects.all()
    productos_serializados = ProductoSerializer(productos, many=True)
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    filas = []
    columnas = []
    if len(productos_serializados.data) == 1:
        for x in productos_serializados.data:
            columnas.append(x)
            filas.append(copy.deepcopy(columnas))
            filas.append([])
    else:
        for x in productos_serializados.data:
            if len(columnas) == 2:
                filas.append(copy.deepcopy(columnas))
                columnas.clear()
            columnas.append(x)
        filas.append(copy.deepcopy(columnas))
    content = render(request, 'productos/list_productos.html', {'productos': filas, 'tamanio_data': len(productos_serializados.data), 'usuario': usuario})
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

@csrf_exempt
def detalle_producto(request, usuario, producto):
    
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    detalle_proveedor = render(request, 'proveedores/detalle_proveedor.html')
    producto_info = Producto.objects.get(id=producto)
    url_detalle_vendedor = '../static/img/detalle_persona.png'
    url_editar = '../editar_proveedor/'
    banner_title = producto_info.nombre
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    content = render(request, 'productos/detalle_producto.html', {
        'url_img': url_detalle_vendedor,
        'url_editar': url_editar,
        'detalle_proveedor': detalle_proveedor.content.decode('utf-8'),
        'producto': producto_info,
        'proveedor': producto_info.proveedor,
        'usuario': usuario

    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
def crear_producto_vista(request, usuario):
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    banner_title = 'Productos'
    #banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        #'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    content = render(request, 'productos/crear_producto.html', {
        'url_peticion': 'crear_producto',
        'campo_1': 'nombre',
        'campo_1_texto': 'Nombre de Producto*',
        'campo_1_tipo': 'text',
        'campo_2': 'proveedor',
        'campo_2_texto': 'Proveedor*',
        'campo_2_tipo': 'text', 
        'campo_3': 'descripcion',
        'campo_3_texto': 'Descripcion*',
        'campo_3_tipo': 'text',
        'campo_4': 'precio',
        'campo_4_texto': 'Precio de Producto*',
        'campo_4_tipo': 'number',
        'campo_5': 'cantidad_disponible',
        'campo_5_texto': 'Cantidad*',
        'campo_5_tipo': 'number',
        'campo_6': 'tiempo_entrega',
        'campo_6_texto': 'Tiempo de estimación de entrega a la mesa*',
        'campo_6_tipo': 'number',
        'campo_7': 'imagen_producto',
        'campo_7_texto': 'Imagen de Producto*',
        'campo_7_tipo': 'file',
        'campo_8': 'activo',
        'campo_8_texto': 'Activo*',
        'campo_8_tipo': 'checkbox',
        'boton_texto': 'AÑADIR'

    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
def editar_producto_vista(request, usuario, producto):
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    banner_title = 'Productos'
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    producto_info = Producto.objects.get(id=producto)
    content = render(request, 'productos/editar_producto.html', {
        'url_peticion': 'editar_producto',
        'campo_1': 'nombre',
        'campo_1_texto': 'Nombre de Producto*',
        'campo_1_tipo': 'text',
        'campo_2': 'proveedor',
        'campo_2_texto': 'Proveedor*',
        'campo_2_tipo': 'text', 
        'campo_3': 'descripcion',
        'campo_3_texto': 'Descripcion*',
        'campo_3_tipo': 'text',
        'campo_4': 'precio',
        'campo_4_texto': 'Precio de Producto*',
        'campo_4_tipo': 'number',
        'campo_5': 'cantidad_disponible',
        'campo_5_texto': 'Cantidad*',
        'campo_5_tipo': 'number',
        'campo_6': 'tiempo_entrega',
        'campo_6_texto': 'Tiempo de estimación de entrega a la mesa*',
        'campo_6_tipo': 'number',
        'campo_7': 'imagen_producto',
        'campo_7_texto': 'Imagen de Producto*',
        'campo_7_tipo': 'file',
        'campo_8': 'activo',
        'campo_8_texto': 'Activo*',
        'campo_8_tipo': 'checkbox',
        'boton_texto': 'EDITAR',
        'producto': producto_info

    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
@api_view(['POST'])
def crear_producto(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    producto = ProductoSerializer(data=jd)
                    if producto.is_valid():
                        producto.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Creación de producto Satisfactoria.'})
                    print(producto.errors)
                    raise ValidationError('Información invalida, verifique los datos.')
            except ValidationError as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e.detail[0])})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['POST'])
def consultar_productos(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    consulta = ProductoConsultaSerializer(data=jd)
                    if not consulta.is_valid() :
                        if consulta.data['proveedor']:
                            proveedor = Proveedor.objects.get(id=consulta.data['proveedor'])
                            consulta = Producto.objects.filter(proveedor=proveedor)
                        else:
                            consulta = Producto.objects.all()
                    else:
                        if consulta.data['proveedor']:
                            proveedor = Proveedor.objects.get(id=consulta.data['proveedor'])
                            consulta = Producto.objects.filter(nombre=consulta['nombre'].value, proveedor=proveedor)
                        else:    
                            consulta = Producto.objects.filter(nombre=consulta['nombre'].value)
                    productos = ProductoSerializer(consulta, many=True)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": productos.data})
            except Proveedor.DoesNotExist:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron productos asociado a ese proveedor'})
            except Producto.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron productos'})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def consultar_producto_editar(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    consulta = ProductoConsultaEditarSerializer(data=jd)
                    if consulta.is_valid() :
                        consulta = Producto.objects.get(id=consulta['id'].value)
                    productos = ProductoSerializer(consulta)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": productos.data})
            except Producto.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron productos'})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def editar_producto(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    producto = ProductoConsultaEditarSerializer(data=jd)
                    if producto.is_valid():
                        producto_actualizar = Producto.objects.get(id=producto['id'].value)
                        producto_actualizar.update_producto(nombre=producto['nombre'].value, descripcion=producto['descripcion'].value, 
                            precio=producto['precio'].value, cantidad_disponible=producto['cantidad_disponible'].value, proveedor=producto['proveedor'].value, 
                            activo=producto['activo'].value)
                        producto_actualizar.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Actualizacion de Producto Satisfactoria.'})
                    else:
                        print(producto.errors)
                        raise ValidationError('Información invalida, verifique los datos.')
            except Producto.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron productos'})
            except ValidationError as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e.detail[0])})
            except Exception as e:
                print(str(e))
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'POST':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(str(e))
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)