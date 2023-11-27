from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import json
@csrf_exempt
@api_view(['POST'])
def crear_proveedor(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    proveedor = ProveedorSerializer(data=jd)
                    if proveedor.is_valid():
                        proveedor.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Creación de Proveedor Satisfactoria.'})
                    else:
                        if 'correo' in proveedor.errors:
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
def consultar_proveedores(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    consulta = ProveedorConsultaSerializer(data=jd)
                    if not consulta.is_valid() :
                        consulta = Proveedor.objects.all()
                    else:
                        consulta = Proveedor.objects.filter(nombre=consulta['nombre'].value)
                    proveedores = ProveedorSerializer(consulta, many=True)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": proveedores.data})
            except Proveedor.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Proveedores'})
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
def consultar_proveedor_editar(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    consulta = ProveedorConsultaEditarSerializer(data=jd)
                    if consulta.is_valid() :
                        consulta = Proveedor.objects.get(id=consulta['id'].value)
                    proveedores = ProveedorSerializer(consulta)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": proveedores.data})
            except Proveedor.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Proveedores'})
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
def editar_proveedor(request):
    try:
        if request.method == 'PUT':
            try:
                jd = json.loads(request.body)
                if jd:
                    proveedor = ProveedorConsultaEditarSerializer(data=jd)
                    if proveedor.is_valid():
                        try:
                            correo_validacion = Proveedor.objects.get(correo=proveedor['correo'].value)
                            if correo_validacion.id != proveedor['id'].value:
                                raise ValidationError('Este correo ya se encuentra registrado, por favor verifique la información suministrada.')
                        except Proveedor.DoesNotExist:
                            pass
                        proveedor_actualizar = Proveedor.objects.get(id=proveedor['id'].value)
                        proveedor_actualizar.update_proveedor(nombre=proveedor['nombre'].value, activo=proveedor['activo'].value, numero_telefono=proveedor['numero_telefono'].value, correo=proveedor['correo'].value, pais=proveedor['pais'].value, codigo_postal=proveedor['codigo_postal'].value, ciudad=proveedor['ciudad'].value, direccion=proveedor['direccion'].value)
                        proveedor_actualizar.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Actualizacion de Proveedor Satisfactoria.'})
                    else:
                        raise ValidationError('Información invalida, verifique los datos.')
            except Proveedor.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Proveedores'})
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
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)