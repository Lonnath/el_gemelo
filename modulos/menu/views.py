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
from django.shortcuts import render
import json
from django.contrib.auth.models import User

def menu(request, usuario):
    
    banner_title = "Menu"
    banner_subtitle = "Nuestro Menu"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_subtitle': banner_subtitle, 
        'banner_texto': banner_texto, 
        'banner_subtexto': banner_subtexto
    })
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    content = render(request, 'menu_content.html')
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


@csrf_exempt
@api_view(['POST'])
def crear_item(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    item = ItemSerializer(data=jd)
                    if item.is_valid():
                        item.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Creación de item Satisfactoria.'})
                    else:
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
def consultar_items(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                consulta = ItemsConsultaSerializer(data=jd)
                if  consulta.is_valid() :
                    consulta = Item.objects.all()
                    out = ItemsConsultaSerializer(consulta, many=True)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": out.data})
                else:
                    return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'La consulta no se pudo realizar.'})
            except Item.DoesNotExist:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Items'})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(str(e))
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def consultar_item_editar(request):
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
@api_view(['PUT'])
def editar_item(request):
    try:
        if request.method == 'PUT':
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