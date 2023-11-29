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
                    else:
                        if 'correo' in producto.errors:
                            raise ValidationError('Este correo ya se encuentra registrado, por favor verifique la información suministrada.')
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
@api_view(['PUT'])
def editar_producto(request):
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