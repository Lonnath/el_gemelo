from django.shortcuts import render
from django.contrib.auth.models import User
from modulos.proveedores.serializers import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from modulos.productos.models import Producto
from decimal import Decimal
import copy

@csrf_exempt
def compras(request, usuario):
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    banner_title = "Compras"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
    })
    compras_info = CompraProductos.objects.all()
    content = render(request, 'compras/list_compra.html', {
        'url_compra': f'../../realizar_compras/{usuario}/',
        'movimientos': compras_info
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
def realizar_compras(request, usuario):
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    banner_title = "Compras"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    
    content = render(request, 'compras/realizar_compra.html', {
        'url_peticion':'realizar_compra',
        'campo_1': 'referencia_producto',
        'campo_1_texto': 'Referencia Producto',
        'campo_1_tipo': 'text',
        'campo_2': 'cantidad',
        'campo_2_texto': 'Cantidad',
        'campo_2_tipo': 'integer', 
        'boton_texto': 'REGISTRAR COMPRA'
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

@csrf_exempt
@api_view(['POST'])
def crear_compra(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    referencia_producto = jd['referencia_producto'] if 'referencia_producto' in jd else None
                    cantidad = jd['cantidad'] if 'cantidad' in jd else None
                    if not referencia_producto or not cantidad:
                        return Response({'CODE' : 2, 'MESSAGE' : 'ERROR', 'DATA' : 'Faltan datos.'})
                    producto = Producto.objects.get(id=referencia_producto)
                    compra_producto = CompraProductos(producto=producto, cantidad=cantidad)
                    compras = CompraProductos.objects.all()
                    compra_producto.referencia_compra = f'CI-{len(compras)}'
                    compra_producto.valor_total = producto.precio*Decimal(cantidad)
                    compra_producto.save()
                    return Response({'CODE' : 1, 'MESSAGE' : 'Ok.', 'DATA' : 'Compra creada con exito'})
            except Exception as e:
                print(str(e))
                return Response({'CODE': 4, "MESSAGE": 'USUARIO NO EXISTE', "DATA": 'Verifique el Usuario de Acceso digitado.'})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def ventas(request, usuario):
    banner_title = "VENTAS"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    ventas_info = VentaProducto.objects.all()
    content = render(request, 'ventas/list_ventas.html', {'movimientos': ventas_info, 'usuario': usuario})
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
def ver_detalle_compra(request, usuario, venta):
    banner_title = "VENTAS"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    ventas_info = VentaProducto.objects.get(id=venta)
    detalles_ventas = DetalleVentaProducto.objects.filter(venta_producto=ventas_info)
    filas = []
    columnas = []
    if len(detalles_ventas) == 1:
        for x in detalles_ventas:
            columnas.append(x)
            filas.append(copy.deepcopy(columnas))
            filas.append([])
    else:
        for x in detalles_ventas:
            if len(columnas) == 2:
                filas.append(copy.deepcopy(columnas))
                columnas.clear()
            columnas.append(x)
        filas.append(copy.deepcopy(columnas))
    valor_devuelto = 0
    for x in detalles_ventas:
        valor_devuelto += x.producto.precio*x.cantidad
    valor_devuelto_out = ventas_info.dinero_ingresado-valor_devuelto 
    content = render(request, 'ventas/detalle_venta.html', {'movimientos': filas, 'usuario': usuario, 'venta': ventas_info, 'dinero_devuelto': valor_devuelto_out})
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
@api_view(['POST'])
def crear_venta(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    productos = jd['productos'] if 'productos' in jd else None
                    dinero_ingresado = jd['dinero_ingresado'] if 'dinero_ingresado' in jd else None
                    if not productos or not dinero_ingresado:
                        return Response({'CODE' : 2, 'MESSAGE' : 'ERROR', 'DATA' : 'Faltan datos.'})
                    venta_producto = VentaProducto()
                    ventas_realizadas = VentaProducto.objects.all()
                    venta_producto.referencia_venta = f'VP-{len(ventas_realizadas)}'
                    venta_producto.dinero_ingresado = dinero_ingresado
                    venta_producto.valor_total = 0
                    venta_producto.save()
                    valor_total = 0
                    for x in productos:
                        producto = Producto.objects.get(id=x['id'])
                        detalle_venta = DetalleVentaProducto()
                        detalle_venta.producto = producto
                        detalle_venta.venta_producto = venta_producto
                        detalle_venta.cantidad = x['cantidad']
                        valor_total += Decimal(x['cantidad']) * producto.precio
                        detalle_venta.save()
                    venta_producto.valor_total = valor_total
                    venta_producto.save()
                    return Response({'CODE' : 1, 'MESSAGE' : 'Ok.', 'DATA' : 'Compra creada con exito'})
            except Exception as e:
                print(str(e))
                return Response({'CODE': 4, "MESSAGE": 'USUARIO NO EXISTE', "DATA": 'Verifique el Usuario de Acceso digitado.'})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def analisis(request, usuario):
    banner_title = "Analisis"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    content = render(request, 'menu_content.html')
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

